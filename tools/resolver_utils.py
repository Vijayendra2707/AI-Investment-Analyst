import re

EXCHANGE_PRIORITY = {

    # USA
    "NASDAQ": 100,
    "NYSE": 95,

    # India
    "NSE": 90,
    "BSE": 90,

    # Europe
    "LSE": 80,
    "XETRA": 75,
    "FRA": 70,

    # Asia
    "HKSE": 70,
    "JPX": 70,

    "Unknown": 0
}


BAD_KEYWORDS = [

    "ETF",
    "FUND",
    "INDEX",
    "TRUST",

    "USD",
    "EUR",
    "GBP",
    "JPY",
    "AUD",
    "CAD",
    "CHF",

    "BTC",
    "ETH",
    "USDT",

    "FOREX",

    "CRYPTO"
]

def is_valid_company(company):

    name = (company["company_name"] or "").upper()

    ticker = (company["ticker"] or "").upper()

    text = f"{name} {ticker}"

    for keyword in BAD_KEYWORDS:

        if keyword in text:
            return False

    return True


def company_initials(name: str) -> str:

    words = re.findall(r"[A-Za-z]+", name)

    if not words:
        return ""

    return "".join(word[0] for word in words).upper()


def score_candidate(company, query):

    score = 0

    query = query.upper().strip()

    ticker = (company["ticker"] or "").upper()

    name = (company["company_name"] or "").upper()

    exchange = (company["exchange"] or "Unknown").upper()

    initials = company_initials(name)

    # ---------------------------------
    # Exchange Priority
    # ---------------------------------

    score += EXCHANGE_PRIORITY.get(exchange, 5)

    # ---------------------------------
    # Exact ticker
    # ---------------------------------

    if ticker == query:

        score += 200

    # ---------------------------------
    # Exact company name
    # ---------------------------------

    if name == query:

        score += 150

    # ---------------------------------
    # Initials
    # Example:
    # Advanced Micro Devices -> AMD
    # ---------------------------------

    if initials == query:

        score += 120

    # ---------------------------------
    # Starts With
    # Example:
    # Tesla -> Tesla Inc.
    # ---------------------------------

    if name.startswith(query):

        score += 80

    # ---------------------------------
    # Whole Word Match
    # Example:
    # Microsoft in "Microsoft Corporation"
    # NOT "Amdocs"
    # ---------------------------------

    words = re.findall(r"[A-Za-z]+", name)

    if query in words:

        score += 60

    return score