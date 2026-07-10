import yfinance as yf

def get_ticker(company_name: str):
    search = yf.Search(company_name, max_results=1)
    
    quotes = search.quotes

    if not quotes:
        return None

    return quotes[0]["symbol"]