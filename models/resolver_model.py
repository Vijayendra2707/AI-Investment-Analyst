from pydantic import BaseModel, Field


class ResolverOutput(BaseModel):

    ticker: str = Field(
        description="Ticker selected from the candidate list."
    )

    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence score."
    )