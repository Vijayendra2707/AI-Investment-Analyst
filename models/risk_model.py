from pydantic import BaseModel


class RiskOutput(BaseModel):

    company_name: str

    risk_score: int

    overall_risk: str

    financial_risks: list[str]

    market_risks: list[str]

    operational_risks: list[str]

    opportunities: list[str]

    summary: str