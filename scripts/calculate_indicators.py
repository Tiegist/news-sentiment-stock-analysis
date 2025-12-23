"""
Script to calculate technical indicators using TA-Lib and PyNance.
"""
import pandas as pd
import numpy as np
try:
    import talib
except ImportError:
    print("TA-Lib not installed. Please install it: pip install TA-Lib")
    talib = None

try:
    import pynance as pn
except ImportError:
    print("PyNance not installed. Please install it: pip install pynance")
    pn = None


def calculate_technical_indicators(df):
    """
    Calculate technical indicators using TA-Lib.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Stock data with columns: Open, High, Low, Close, Volume
    
    Returns:
    --------
    pd.DataFrame
        Data with added technical indicators
    """
    if df is None or df.empty:
        return df
    
    if talib is None:
        print("TA-Lib is not available. Using basic calculations.")
        return calculate_basic_indicators(df)
    
    df_indicators = df.copy()
    
    # Ensure we have the required columns
    required_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    for col in required_cols:
        if col not in df_indicators.columns:
            print(f"Warning: {col} column not found")
            return df_indicators
    
    # Convert to numpy arrays for TA-Lib
    open_prices = df_indicators['Open'].values
    high_prices = df_indicators['High'].values
    low_prices = df_indicators['Low'].values
    close_prices = df_indicators['Close'].values
    volume = df_indicators['Volume'].values
    
    # Moving Averages
    df_indicators['SMA_20'] = talib.SMA(close_prices, timeperiod=20)
    df_indicators['SMA_50'] = talib.SMA(close_prices, timeperiod=50)
    df_indicators['EMA_12'] = talib.EMA(close_prices, timeperiod=12)
    df_indicators['EMA_26'] = talib.EMA(close_prices, timeperiod=26)
    
    # RSI (Relative Strength Index)
    df_indicators['RSI'] = talib.RSI(close_prices, timeperiod=14)
    
    # MACD (Moving Average Convergence Divergence)
    macd, macdsignal, macdhist = talib.MACD(close_prices, fastperiod=12, 
                                            slowperiod=26, signalperiod=9)
    df_indicators['MACD'] = macd
    df_indicators['MACD_signal'] = macdsignal
    df_indicators['MACD_hist'] = macdhist
    
    # Bollinger Bands
    upper, middle, lower = talib.BBANDS(close_prices, timeperiod=20, 
                                         nbdevup=2, nbdevdn=2, matype=0)
    df_indicators['BB_upper'] = upper
    df_indicators['BB_middle'] = middle
    df_indicators['BB_lower'] = lower
    
    # Stochastic Oscillator
    slowk, slowd = talib.STOCH(high_prices, low_prices, close_prices,
                                fastk_period=14, slowk_period=3, 
                                slowd_period=3)
    df_indicators['Stoch_K'] = slowk
    df_indicators['Stoch_D'] = slowd
    
    # Average True Range (ATR)
    df_indicators['ATR'] = talib.ATR(high_prices, low_prices, close_prices, timeperiod=14)
    
    # On Balance Volume (OBV)
    df_indicators['OBV'] = talib.OBV(close_prices, volume)
    
    return df_indicators


def calculate_basic_indicators(df):
    """
    Calculate basic technical indicators without TA-Lib.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Stock data with columns: Open, High, Low, Close, Volume
    
    Returns:
    --------
    pd.DataFrame
        Data with added basic indicators
    """
    df_indicators = df.copy()
    
    if 'Close' not in df_indicators.columns:
        return df_indicators
    
    # Simple Moving Averages
    df_indicators['SMA_20'] = df_indicators['Close'].rolling(window=20).mean()
    df_indicators['SMA_50'] = df_indicators['Close'].rolling(window=50).mean()
    
    # Exponential Moving Averages
    df_indicators['EMA_12'] = df_indicators['Close'].ewm(span=12, adjust=False).mean()
    df_indicators['EMA_26'] = df_indicators['Close'].ewm(span=26, adjust=False).mean()
    
    # RSI calculation
    delta = df_indicators['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df_indicators['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    df_indicators['MACD'] = df_indicators['EMA_12'] - df_indicators['EMA_26']
    df_indicators['MACD_signal'] = df_indicators['MACD'].ewm(span=9, adjust=False).mean()
    df_indicators['MACD_hist'] = df_indicators['MACD'] - df_indicators['MACD_signal']
    
    # Bollinger Bands
    df_indicators['BB_middle'] = df_indicators['Close'].rolling(window=20).mean()
    bb_std = df_indicators['Close'].rolling(window=20).std()
    df_indicators['BB_upper'] = df_indicators['BB_middle'] + (bb_std * 2)
    df_indicators['BB_lower'] = df_indicators['BB_middle'] - (bb_std * 2)
    
    return df_indicators


if __name__ == "__main__":
    print("Technical indicators calculation script")
    print("Use this script to calculate indicators for stock data")

