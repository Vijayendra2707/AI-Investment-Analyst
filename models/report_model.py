from pydantic import BaseModel, Field


class ReportOutput(BaseModel):

    company: str = Field(
        description="Company analyzed."
    )

    executive_summary: str = Field(
        description="Overall summary of the investment analysis."
    )

    news_summary: str = Field(
        description="Summary of recent news."
    )

    financial_summary: str = Field(
        description="Summary of financial health."
    )

    risk_summary: str = Field(
        description="Summary of the identified risks."
    )

    recommendation: str = Field(
        description="Buy, Hold, Sell or similar recommendation."
    )

    confidence: str = Field(
        description="Confidence level: High, Medium or Low."
    )

    conclusion: str = Field(
        description="Final investment conclusion."
    )