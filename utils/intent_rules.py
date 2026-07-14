from models.workflow import Workflow


NEWS_KEYWORDS = [
    "news",
    "headline",
    "headlines",
    "latest",
    "recent",
    "update",
    "updates",
]

FINANCE_KEYWORDS = [
    "financial",
    "financials",
    "finance",
    "revenue",
    "profit",
    "income",
    "balance sheet",
    "cash flow",
    "earnings",
    "eps",
    "pe",
    "p/e",
    "roe",
    "market cap",
    "valuation",
]

COMPARISON_KEYWORDS = [
    "compare",
    "comparison",
    "versus",
    "vs",
    "against",
]

INVESTMENT_KEYWORDS = [
    "analyze",
    "analyse",
    "analysis",
    "evaluate",
    "assessment",
    "review",
    "invest",
    "investment",
    "recommend",
    "recommendation",
    "risk",
    "swot",
    "overview",
]


def detect_workflow(query: str) -> Workflow | None:

    q = query.lower()

    has_news = any(word in q for word in NEWS_KEYWORDS)
    has_finance = any(word in q for word in FINANCE_KEYWORDS)
    has_comparison = any(word in q for word in COMPARISON_KEYWORDS)
    has_investment = any(word in q for word in INVESTMENT_KEYWORDS)

    if has_comparison:
        return Workflow.COMPARISON

    if has_news and has_finance:
        return Workflow.NEWS_FINANCE

    if has_news:
        return Workflow.NEWS

    if has_finance:
        return Workflow.FINANCE

    if has_investment:
        return Workflow.INVESTMENT

    return None