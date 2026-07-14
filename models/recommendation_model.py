from pydantic import BaseModel, Field


class RecommendationOutput(BaseModel):

    company_name: str = Field(
        description="Company being evaluated."
    )

    recommendation: str = Field(
        description="Investment recommendation: BUY, HOLD, or SELL."
    )

    confidence: int = Field(
        ge=0,
        le=100,
        description="Confidence in the investment recommendation from 0 to 100."
    )

    investment_horizon: str = Field(
        description="Suggested investment horizon: Short Term, Medium Term, or Long Term."
    )

    reasons: list[str] = Field(
        description="Primary reasons supporting the recommendation."
    )

    concerns: list[str] = Field(
        description="Key concerns investors should continue monitoring."
    )

    summary: str = Field(
        description="Concise investment recommendation summary."
    )