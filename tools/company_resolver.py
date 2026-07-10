import os
import requests

from dotenv import load_dotenv

from tools.resolver_utils import is_valid_company, score_candidate

load_dotenv()

API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/stable"

def search_by_symbol(query: str):

    url = (
        f"{BASE_URL}/search-symbol"
        f"?query={query}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json()

def search_by_name(query: str):

    url = (
        f"{BASE_URL}/search-name"
        f"?query={query}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json()

def normalize_company(company):

    exchange = (
        company.get("exchangeShortName")
        or company.get("exchange")
        or company.get("stockExchange")
        or "Unknown"
    )
     
    return {

        "ticker": company.get("symbol"),

        "company_name": company.get("name"),

        "exchange": exchange
    }
def search_companies(query: str):

    symbol_results = search_by_symbol(query)

    name_results = search_by_name(query)

    merged = []

    for company in symbol_results:

        merged.append(
            normalize_company(company)
        )

    for company in name_results:

        merged.append(
            normalize_company(company)
        )

        merged = remove_duplicates(merged)

        merged = [

        company

        for company in merged

        if is_valid_company(company)

    ]

    # ------------------------
    # Score every company
    # ------------------------

    for company in merged:

        company["score"] = score_candidate(

            company,

            query

        )

    # ------------------------
    # Highest score first
    # ------------------------

    merged.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    # ------------------------
    # Keep only Top 5
    # ------------------------

    return merged[:5]

def remove_duplicates(companies):

    seen = set()

    unique = []

    for company in companies:

        ticker = company["ticker"]

        if ticker in seen:

            continue

        seen.add(ticker)

        unique.append(company)

    return unique