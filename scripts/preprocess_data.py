"""
Script for data cleaning and preprocessing.
"""
import pandas as pd
import numpy as np
from datetime import datetime


def clean_news_data(df):
    """
    Clean and preprocess news data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw news data
    
    Returns:
    --------
    pd.DataFrame
        Cleaned news data
    """
    if df is None or df.empty:
        return df
    
    # Create a copy to avoid modifying original
    df_clean = df.copy()
    
    # Remove duplicates
    df_clean = df_clean.drop_duplicates(subset=['headline', 'date', 'stock'], keep='first')
    
    # Remove rows with missing headlines
    df_clean = df_clean.dropna(subset=['headline'])
    
    # Remove rows with empty headlines
    df_clean = df_clean[df_clean['headline'].str.strip() != '']
    
    # Ensure date is datetime
    if 'date' in df_clean.columns:
        df_clean['date'] = pd.to_datetime(df_clean['date'], errors='coerce')
        df_clean = df_clean.dropna(subset=['date'])
    
    # Extract date only (remove time if needed for alignment)
    df_clean['date_only'] = df_clean['date'].dt.date
    
    # Calculate headline length
    df_clean['headline_length'] = df_clean['headline'].str.len()
    
    # Extract hour of publication if time is available
    if 'date' in df_clean.columns:
        df_clean['publication_hour'] = df_clean['date'].dt.hour
        df_clean['publication_day'] = df_clean['date'].dt.day_name()
    
    return df_clean


def clean_stock_data(df):
    """
    Clean and preprocess stock price data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw stock data
    
    Returns:
    --------
    pd.DataFrame
        Cleaned stock data
    """
    if df is None or df.empty:
        return df
    
    df_clean = df.copy()
    
    # Ensure Date column exists
    if 'Date' in df_clean.columns:
        df_clean['Date'] = pd.to_datetime(df_clean['Date'], errors='coerce')
    elif 'date' in df_clean.columns:
        df_clean['date'] = pd.to_datetime(df_clean['date'], errors='coerce')
    
    # Remove rows with missing critical data
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in required_cols:
        if col in df_clean.columns:
            df_clean = df_clean.dropna(subset=[col])
    
    # Calculate daily returns
    if 'Close' in df_clean.columns:
        df_clean['daily_return'] = df_clean['Close'].pct_change()
        df_clean['daily_return_pct'] = df_clean['daily_return'] * 100
    
    return df_clean


if __name__ == "__main__":
    print("Data preprocessing script")
    print("Use this script to clean and preprocess your data")

