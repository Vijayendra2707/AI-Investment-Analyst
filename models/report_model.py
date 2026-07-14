from pydantic import BaseModel, Field


class ReportOutput(BaseModel):

    company: str = Field(
        description="Company analyzed."
    )

    executive_summary: str = Field(
        description="High-level summary of the complete investment analysis."
    )

    news_summary: str = Field(
        description="Summary of the recent news analysis."
    )

    financial_summary: str = Field(
        description="Summary of the financial analysis."
    )

    risk_summary: str = Field(
        description="Summary of the investment risks."
    )

    recommendation_summary: str = Field(
        description="Summary of the investment recommendation."
    )

    overall_confidence: str = Field(
        description="Overall confidence level of the complete report: High, Medium, or Low."
    )

    conclusion: str = Field(
        description="Final investment conclusion."
    )