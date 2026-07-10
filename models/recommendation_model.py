from pydantic import BaseModel

class RecommendationOutput(BaseModel):

    company_name: str

    recommendation: str

    confidence: int

    investment_horizon: str

    reasons: list[str]

    concerns: list[str]

    summary: str