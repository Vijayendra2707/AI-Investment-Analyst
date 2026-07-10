import yfinance as yf
from tools.ticker_tool import get_ticker

def get_financial_data(company: str):
    ticker = get_ticker(company)

    if ticker is None:
        return None
    
    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "company": info.get("longName"),
        "symbol": info.get("symbol"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "currentPrice": info.get("currentPrice"),
        "marketCap": info.get("marketCap"),
        "trailingPE": info.get("trailingPE"),
        "forwardPE": info.get("forwardPE"),
        "revenueGrowth": info.get("revenueGrowth"),
        "earningsGrowth": info.get("earningsGrowth"),
        "returnOnEquity": info.get("returnOnEquity"),
        "debtToEquity": info.get("debtToEquity"),
    }