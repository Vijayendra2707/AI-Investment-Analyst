from pydantic import BaseModel, Field


class ComparisonOutput(BaseModel):

    executive_summary: str = Field(
        description="High level summary of the comparison."
    )

    financial_comparison: str = Field(
        description="Comparison of financial performance."
    )

    news_comparison: str = Field(
        description="Comparison of recent news and sentiment."
    )

    strengths: dict[str, list[str]] = Field(
        description="Strengths of each company."
    )

    weaknesses: dict[str, list[str]] = Field(
        description="Weaknesses of each company."
    )

    winner: str = Field(
        description="Best investment opportunity."
    )

    recommendation: str = Field(
        description="Final recommendation."
    )

    confidence: str = Field(
        description="Confidence level."
    )

    conclusion: str = Field(
        description="Final conclusion."
    )