import pandas as pd 
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("financial_modeling_prep_api_key")


def get_dataframe(*, ticker: str):
    url = f"https://financialmodelingprep.com/stable/historical-price-eod/light?symbol={ticker}&apikey={API_KEY}"
    data = requests.get(url)
    df = pd.DataFrame(data.json())
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df = df[["price"]]
    df.rename(columns={"price": f"{ticker}_price"}, inplace=True)
    
    return df

available_tickers = [
    "AAPL", "TSLA", "AMZN", "MSFT", "NVDA", "GOOGL", "META", "NFLX", "JPM", "V",
    "BAC", "AMD", "PYPL", "DIS", "T", "PFE", "COST", "INTC", "KO", "TGT",
    "NKE", "SPY", "BA", "BABA", "XOM", "WMT", "GE", "CSCO", "VZ", "JNJ",
    "CVX", "PLTR", "SQ", "SHOP", "SBUX", "SOFI", "HOOD", "RBLX", "SNAP", "AMD",
    "UBER", "FDX", "ABBV", "ETSY", "MRNA", "LMT", "GM", "F", "RIVN", "LCID",
    "CCL", "DAL", "UAL", "AAL", "TSM", "SONY", "ET", "NOK", "MRO", "COIN",
    "RIVN", "SIRI", "SOFI", "RIOT", "CPRX", "PYPL", "TGT", "VWO", "SPYG", "NOK",
    "ROKU", "HOOD", "VIAC", "ATVI", "BIDU", "DOCU", "ZM", "PINS", "TLRY", "WBA",
    "VIAC", "MGM", "NFLX", "NIO", "C", "GS", "WFC", "ADBE", "PEP", "UNH",
    "CARR", "FUBO", "HCA", "TWTR", "BILI", "SIRI", "VIAC", "FUBO", "RKT"
]


def is_ticker_aviable(*, ticker: str):
    return ticker in available_tickers