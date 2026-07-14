from pydantic import BaseModel, Field


class ComparisonOutput(BaseModel):

    executive_summary: str = Field(
        description="High-level summary of the comparison."
    )

    financial_comparison: str = Field(
        description="Comparison of the companies' financial performance."
    )

    news_comparison: str = Field(
        description="Comparison of recent news, sentiment, and major events."
    )

    strengths: dict[str, list[str]] = Field(
        description="Key strengths for each company."
    )

    weaknesses: dict[str, list[str]] = Field(
        description="Key weaknesses for each company."
    )

    winner: str = Field(
        description="Company that performs best overall based on the supplied analyses."
    )

    recommendation: str = Field(
        description="Investment recommendation explaining why the winner should or should not be preferred."
    )

    confidence: str = Field(
        description="Overall confidence level: High, Medium, or Low."
    )

    conclusion: str = Field(
        description="Final comparison conclusion."
    )