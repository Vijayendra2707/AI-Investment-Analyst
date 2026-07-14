import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FMP_API_KEY")
BASE_URL = "https://financialmodelingprep.com/stable"

if not API_KEY:
    raise ValueError("FMP_API_KEY not found in environment variables.")


def _get(endpoint: str, params: dict | None = None) -> list | dict:
    """
    Generic helper for making requests to Financial Modeling Prep.
    """

    if params is None:
        params = {}

    params["apikey"] = API_KEY

    response = requests.get(
        f"{BASE_URL}/{endpoint}",
        params=params,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()


def get_company_profile(ticker: str) -> dict:
    data = _get(
        "profile",
        {
            "symbol": ticker
        }
    )

    return data[0] if data else {}


def get_income_statement(ticker: str) -> dict:
    data = _get(
        "income-statement",
        {
            "symbol": ticker,
            "limit": 1
        }
    )

    return data[0] if data else {}


def get_ratios(ticker: str) -> dict:
    data = _get(
        "ratios",
        {
            "symbol": ticker,
            "limit": 1
        }
    )

    return data[0] if data else {}


def get_financial_data(ticker: str) -> dict:
    """
    Fetch and combine financial information for a company.
    """

    try:
        profile = get_company_profile(ticker)
    except Exception:
        profile = {}

    try:
        income = get_income_statement(ticker)
    except Exception:
        income = {}

    try:
        ratios = get_ratios(ticker)
    except Exception:
        ratios = {}

    return {
        "company": profile.get("companyName"),
        "sector": profile.get("sector"),
        "industry": profile.get("industry"),

        "price": profile.get("price"),

        "market_cap": (
            profile.get("mktCap")
            or profile.get("marketCap")
        ),

        "revenue": income.get("revenue"),
        "net_income": income.get("netIncome"),
        "eps": income.get("eps"),

        "pe_ratio": ratios.get("priceEarningsRatio"),
        "roe": ratios.get("returnOnEquity"),
    }