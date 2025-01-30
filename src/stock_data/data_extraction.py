import os

import requests
import yfinance as yf

from dotenv import load_dotenv

load_dotenv()  

CERTIFICATE_PATH = os.getenv("CERTIFICATE_PATH")
def get_stock_data(ticker: str) -> str:
    """Fetch basic stock info and recent price data using yfinance.
    
    Args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'TSLA').
        
    Returns:
        str: A formatted string containing stock data.
    """
    try:
        session = requests.Session()
        session.verify = CERTIFICATE_PATH
        stock = yf.Ticker(ticker)
        info = stock.info 
        
        current_price = info.get('regularMarketPrice', 'N/A')
        previous_close = info.get('regularMarketPreviousClose', 'N/A')
        market_cap = info.get('marketCap', 'N/A')
        short_ratio = info.get('shortRatio', 'N/A')

        response = (
            f"**{ticker.upper()} Stock Data**\n"
            f"- Current Price: {current_price}\n"
            f"- Previous Close: {previous_close}\n"
            f"- Market Cap: {market_cap}\n"
            f"- Short Ratio: {short_ratio}\n"
        )
        return response
    
    except ValueError as e:
        return f"Error fetching data for {ticker}: {str(e)}. Please check the ticker and try again."
    # except Exception as e:
    #     return f"Error fetching data for {ticker}: {str(e)}. "
