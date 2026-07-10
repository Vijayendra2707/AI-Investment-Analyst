from pydantic import BaseModel, Field

class NewsOutput(BaseModel):

    company_overview: str = Field(
        description="Short description of the company"
    )

    recent_news: list[str] = Field(
        description="Important recent news"
    )

    opportunities: list[str] = Field(
        description="Potential opportunities"
    )

    risks: list[str] = Field(
        description="Risks identified from the news"
    )

    investor_impact: str = Field(
        description="Overall impact on investors"
    )