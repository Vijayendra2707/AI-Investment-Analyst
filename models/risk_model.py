from pydantic import BaseModel, Field


class RiskOutput(BaseModel):

    company_name: str = Field(
        description="Company being analyzed."
    )

    risk_score: int = Field(
        ge=0,
        le=100,
        description="Overall investment risk score from 0 (lowest risk) to 100 (highest risk)."
    )

    overall_risk: str = Field(
        description="Overall risk category: Very Low, Low, Moderate, High, or Very High."
    )

    financial_risks: list[str] = Field(
        description="Major financial risks."
    )

    market_risks: list[str] = Field(
        description="Major market and industry risks."
    )

    operational_risks: list[str] = Field(
        description="Major operational and execution risks."
    )

    opportunities: list[str] = Field(
        description="Potential opportunities despite the identified risks."
    )

    summary: str = Field(
        description="Concise investment-oriented risk summary."
    )