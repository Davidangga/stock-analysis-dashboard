import numpy
import yfinance as yf
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Constant variables
load_dotenv()
api_key = os.getenv("API_KEY")

# Extracting data from third party

def news_data_fetch(stock):
    # Complete: fetching by popularity 

def stock_data_fetch(symbol):
    
    # Fix limit to only allow US stock
    end = datetime.now()
    start = end - timedelta(days=6*30)
    ticker = yf.Ticker(symbol)
    ticker_data = ticker.history(period="1d", start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d"))
    
    # FIX: Some company didn't put their balance sheet data
    ticker_balance_sheet = ticker.balance_sheet
    return ticker_data["Close"], ticker_data["Volume"], ticker_balance_sheet