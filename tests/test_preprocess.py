"""
Unit tests for data preprocessing functions.
"""
import pytest
import pandas as pd
import numpy as np
from datetime import datetime
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from preprocess_data import clean_news_data, clean_stock_data


class TestNewsDataCleaning:
    """Test cases for news data cleaning."""
    
    def test_remove_duplicates(self):
        """Test that duplicates are removed."""
        df = pd.DataFrame({
            'headline': ['Test headline', 'Test headline', 'Another headline'],
            'date': ['2024-01-01', '2024-01-01', '2024-01-02'],
            'stock': ['AAPL', 'AAPL', 'MSFT']
        })
        result = clean_news_data(df)
        assert len(result) == 2
    
    def test_remove_missing_headlines(self):
        """Test that rows with missing headlines are removed."""
        df = pd.DataFrame({
            'headline': ['Test headline', None, 'Another headline', ''],
            'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-03'],
            'stock': ['AAPL', 'AAPL', 'MSFT', 'GOOGL']
        })
        result = clean_news_data(df)
        assert len(result) == 2
        assert result['headline'].isna().sum() == 0
    
    def test_headline_length_calculation(self):
        """Test that headline length is calculated."""
        df = pd.DataFrame({
            'headline': ['Test headline', 'Another headline'],
            'date': ['2024-01-01', '2024-01-02'],
            'stock': ['AAPL', 'MSFT']
        })
        result = clean_news_data(df)
        assert 'headline_length' in result.columns
        assert result['headline_length'].iloc[0] == len('Test headline')


class TestStockDataCleaning:
    """Test cases for stock data cleaning."""
    
    def test_daily_return_calculation(self):
        """Test that daily returns are calculated."""
        df = pd.DataFrame({
            'Date': pd.date_range('2024-01-01', periods=5),
            'Open': [100, 101, 102, 103, 104],
            'High': [105, 106, 107, 108, 109],
            'Low': [99, 100, 101, 102, 103],
            'Close': [101, 102, 103, 104, 105],
            'Volume': [1000, 1100, 1200, 1300, 1400]
        })
        result = clean_stock_data(df)
        assert 'daily_return' in result.columns
        assert not pd.isna(result['daily_return'].iloc[0])  # First should be NaN
        assert not pd.isna(result['daily_return'].iloc[1])  # Second should have value
    
    def test_remove_missing_critical_data(self):
        """Test that rows with missing critical data are removed."""
        df = pd.DataFrame({
            'Date': pd.date_range('2024-01-01', periods=3),
            'Open': [100, None, 102],
            'High': [105, 106, None],
            'Low': [99, 100, 101],
            'Close': [101, 102, 103],
            'Volume': [1000, 1100, 1200]
        })
        result = clean_stock_data(df)
        # Should remove rows with missing Open or High
        assert result['Open'].isna().sum() == 0
        assert result['High'].isna().sum() == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

