from pydantic import BaseModel, Field


class FinanceOutput(BaseModel):

    financial_health: str = Field(
        description="Overall assessment of the company's financial condition."
    )

    growth_potential: str = Field(
        description="Assessment of the company's future growth prospects."
    )

    profitability: str = Field(
        description="Evaluation of earnings, margins, and overall profitability."
    )

    valuation: str = Field(
        description="Assessment of whether the company appears undervalued, fairly valued, or overvalued."
    )

    strengths: list[str] = Field(
        description="Key financial strengths identified from the supplied financial data."
    )

    weaknesses: list[str] = Field(
        description="Key financial weaknesses identified from the supplied financial data."
    )

    summary: str = Field(
        description="Concise investment-oriented summary of the company's financial position."
    )