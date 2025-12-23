"""
Script to analyze correlation between news sentiment and stock returns.
"""
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt
import seaborn as sns


def align_dates(news_df, stock_df, news_date_col='date', stock_date_col='Date'):
    """
    Align news and stock data by dates.
    
    Parameters:
    -----------
    news_df : pd.DataFrame
        News data with date and sentiment columns
    stock_df : pd.DataFrame
        Stock data with date and return columns
    news_date_col : str
        Name of date column in news dataframe
    stock_date_col : str
        Name of date column in stock dataframe
    
    Returns:
    --------
    pd.DataFrame
        Merged dataframe with aligned dates
    """
    # Ensure dates are datetime
    news_df[news_date_col] = pd.to_datetime(news_df[news_date_col])
    stock_df[stock_date_col] = pd.to_datetime(stock_df[stock_date_col])
    
    # Extract date only (remove time)
    news_df['date_only'] = news_df[news_date_col].dt.date
    stock_df['date_only'] = stock_df[stock_date_col].dt.date
    
    # Merge on date
    merged = pd.merge(
        news_df,
        stock_df,
        on='date_only',
        how='inner',
        suffixes=('_news', '_stock')
    )
    
    return merged


def aggregate_daily_sentiment(df, date_col='date_only', 
                              sentiment_col='sentiment_polarity',
                              stock_col='stock'):
    """
    Aggregate sentiment scores by day and stock.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataframe with sentiment and date columns
    date_col : str
        Name of date column
    sentiment_col : str
        Name of sentiment polarity column
    stock_col : str
        Name of stock symbol column
    
    Returns:
    --------
    pd.DataFrame
        Daily aggregated sentiment scores
    """
    daily_sentiment = df.groupby([date_col, stock_col]).agg({
        sentiment_col: ['mean', 'std', 'count'],
        'sentiment_label': lambda x: x.mode()[0] if len(x.mode()) > 0 else 'neutral'
    }).reset_index()
    
    # Flatten column names
    daily_sentiment.columns = [
        date_col, stock_col, 'avg_sentiment', 'std_sentiment', 
        'article_count', 'dominant_sentiment'
    ]
    
    return daily_sentiment


def calculate_correlation(sentiment_scores, stock_returns, 
                          sentiment_col='avg_sentiment',
                          return_col='daily_return'):
    """
    Calculate correlation between sentiment and stock returns.
    
    Parameters:
    -----------
    sentiment_scores : pd.Series or array
        Sentiment scores
    stock_returns : pd.Series or array
        Stock returns
    sentiment_col : str
        Name of sentiment column (if dataframe)
    return_col : str
        Name of return column (if dataframe)
    
    Returns:
    --------
    dict
        Dictionary with correlation metrics
    """
    # Handle Series/DataFrame inputs
    if isinstance(sentiment_scores, pd.DataFrame):
        sentiment_scores = sentiment_scores[sentiment_col]
    if isinstance(stock_returns, pd.DataFrame):
        stock_returns = stock_returns[return_col]
    
    # Remove NaN values
    valid_mask = ~(pd.isna(sentiment_scores) | pd.isna(stock_returns))
    sentiment_clean = sentiment_scores[valid_mask]
    returns_clean = stock_returns[valid_mask]
    
    if len(sentiment_clean) < 2:
        return {
            'pearson_corr': np.nan,
            'pearson_pvalue': np.nan,
            'spearman_corr': np.nan,
            'spearman_pvalue': np.nan,
            'n_observations': len(sentiment_clean)
        }
    
    # Calculate Pearson correlation
    pearson_corr, pearson_p = pearsonr(sentiment_clean, returns_clean)
    
    # Calculate Spearman correlation
    spearman_corr, spearman_p = spearmanr(sentiment_clean, returns_clean)
    
    return {
        'pearson_corr': pearson_corr,
        'pearson_pvalue': pearson_p,
        'spearman_corr': spearman_corr,
        'spearman_pvalue': spearman_p,
        'n_observations': len(sentiment_clean)
    }


def visualize_correlation(sentiment_scores, stock_returns, 
                          sentiment_col='avg_sentiment',
                          return_col='daily_return',
                          title='Sentiment vs Stock Returns'):
    """
    Visualize correlation between sentiment and stock returns.
    
    Parameters:
    -----------
    sentiment_scores : pd.Series or array
        Sentiment scores
    stock_returns : pd.Series or array
        Stock returns
    sentiment_col : str
        Name of sentiment column (if dataframe)
    return_col : str
        Name of return column (if dataframe)
    title : str
        Plot title
    """
    # Handle Series/DataFrame inputs
    if isinstance(sentiment_scores, pd.DataFrame):
        sentiment_scores = sentiment_scores[sentiment_col]
    if isinstance(stock_returns, pd.DataFrame):
        stock_returns = stock_returns[return_col]
    
    # Remove NaN values
    valid_mask = ~(pd.isna(sentiment_scores) | pd.isna(stock_returns))
    sentiment_clean = sentiment_scores[valid_mask]
    returns_clean = stock_returns[valid_mask]
    
    # Calculate correlation
    corr_results = calculate_correlation(sentiment_clean, returns_clean)
    
    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Scatter plot
    axes[0].scatter(sentiment_clean, returns_clean, alpha=0.5, s=20)
    axes[0].set_xlabel('Average Sentiment Score')
    axes[0].set_ylabel('Daily Stock Return (%)')
    axes[0].set_title(f'{title}\nPearson r={corr_results["pearson_corr"]:.3f}, p={corr_results["pearson_pvalue"]:.3f}')
    axes[0].grid(True, alpha=0.3)
    
    # Add trend line
    z = np.polyfit(sentiment_clean, returns_clean, 1)
    p = np.poly1d(z)
    axes[0].plot(sentiment_clean, p(sentiment_clean), "r--", alpha=0.8, linewidth=2)
    
    # Time series plot
    axes[1].plot(range(len(sentiment_clean)), sentiment_clean, 
                 label='Sentiment', alpha=0.7, linewidth=1.5)
    ax2 = axes[1].twinx()
    ax2.plot(range(len(returns_clean)), returns_clean, 
             label='Returns', color='orange', alpha=0.7, linewidth=1.5)
    axes[1].set_xlabel('Time (days)')
    axes[1].set_ylabel('Average Sentiment Score', color='blue')
    ax2.set_ylabel('Daily Stock Return (%)', color='orange')
    axes[1].set_title('Sentiment and Returns Over Time')
    axes[1].tick_params(axis='y', labelcolor='blue')
    ax2.tick_params(axis='y', labelcolor='orange')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return corr_results


if __name__ == "__main__":
    print("Correlation analysis script")
    print("Use this script to analyze correlation between sentiment and stock returns")

