import os

import yfinance as yf
import requests

from dotenv import load_dotenv

load_dotenv()

session = requests.Session()
session.verify = os.getenv("CERTIFICATE_PATH")

stock = yf.Ticker("AAPL", session=session)
print(stock.info)