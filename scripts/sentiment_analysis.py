"""
Script to perform sentiment analysis on news headlines.
"""
import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk

# Download required NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('brown', quiet=True)
except:
    pass


def analyze_sentiment(text):
    """
    Analyze sentiment of a text using TextBlob.
    
    Parameters:
    -----------
    text : str
        Text to analyze
    
    Returns:
    --------
    dict
        Dictionary with polarity, subjectivity, and sentiment label
    """
    if pd.isna(text) or text == '':
        return {
            'polarity': 0.0,
            'subjectivity': 0.0,
            'sentiment': 'neutral'
        }
    
    try:
        blob = TextBlob(str(text))
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Classify sentiment
        if polarity > 0.1:
            sentiment = 'positive'
        elif polarity < -0.1:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'polarity': polarity,
            'subjectivity': subjectivity,
            'sentiment': sentiment
        }
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return {
            'polarity': 0.0,
            'subjectivity': 0.0,
            'sentiment': 'neutral'
        }


def add_sentiment_scores(df, text_column='headline'):
    """
    Add sentiment scores to a dataframe.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataframe with text column
    text_column : str
        Name of the column containing text to analyze
    
    Returns:
    --------
    pd.DataFrame
        Dataframe with added sentiment columns
    """
    if df is None or df.empty:
        return df
    
    if text_column not in df.columns:
        print(f"Column '{text_column}' not found in dataframe")
        return df
    
    print("Analyzing sentiment... This may take a while for large datasets.")
    
    # Apply sentiment analysis
    sentiment_results = df[text_column].apply(analyze_sentiment)
    
    # Extract results
    df['sentiment_polarity'] = sentiment_results.apply(lambda x: x['polarity'])
    df['sentiment_subjectivity'] = sentiment_results.apply(lambda x: x['subjectivity'])
    df['sentiment_label'] = sentiment_results.apply(lambda x: x['sentiment'])
    
    print("Sentiment analysis complete!")
    print(f"\nSentiment distribution:")
    print(df['sentiment_label'].value_counts())
    
    return df


if __name__ == "__main__":
    print("Sentiment analysis script")
    print("Use this script to analyze sentiment of news headlines")

