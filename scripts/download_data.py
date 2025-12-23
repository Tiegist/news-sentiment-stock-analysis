"""
Script to download financial news and stock price data.
"""
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os


def download_stock_data(symbol, start_date, end_date):
    """
    Download stock price data for a given symbol.
    
    Parameters:
    -----------
    symbol : str
        Stock ticker symbol (e.g., 'AAPL')
    start_date : str
        Start date in 'YYYY-MM-DD' format
    end_date : str
        End date in 'YYYY-MM-DD' format
    
    Returns:
    --------
    pd.DataFrame
        Stock price data with columns: Open, High, Low, Close, Volume
    """
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        data.reset_index(inplace=True)
        return data
    except Exception as e:
        print(f"Error downloading data for {symbol}: {e}")
        return None


def load_news_data(file_path):
    """
    Load financial news data from a CSV or JSON file.
    
    Parameters:
    -----------
    file_path : str
        Path to the news data file
    
    Returns:
    --------
    pd.DataFrame
        News data with columns: headline, url, publisher, date, stock
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print("Please ensure the news data file is available.")
        return None
    
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            print(f"Unsupported file format: {file_path}")
            return None
        
        # Ensure date column is datetime
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'])
        
        return df
    except Exception as e:
        print(f"Error loading news data: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    print("Data download script")
    print("Please use this script to download stock data and load news data")

