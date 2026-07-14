from pydantic import BaseModel, Field


class NewsOutput(BaseModel):

    news_summary: str = Field(
        description="Concise summary of the recent news."
    )

    key_events: list[str] = Field(
        description="Most important recent events affecting the company."
    )

    opportunities: list[str] = Field(
        description="Positive developments or opportunities identified from the news."
    )

    risks: list[str] = Field(
        description="Potential risks or concerns identified from the news."
    )

    investor_impact: str = Field(
        description="Overall impact of the recent news on investors."
    )