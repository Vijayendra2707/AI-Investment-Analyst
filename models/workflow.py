from enum import Enum


class Workflow(str, Enum):

    INVESTMENT = "investment"

    NEWS = "news"

    FINANCE = "finance"

    NEWS_FINANCE = "news_finance"

    COMPARISON = "comparison"