from pydantic import BaseModel


class FinanceOutput(BaseModel):

    company_name: str

    overall_health: str

    revenue_growth: str

    profitability: str

    valuation: str

    strengths: list[str]

    weaknesses: list[str]

    summary: str