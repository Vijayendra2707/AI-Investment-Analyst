from pydantic import BaseModel, Field


class IntentOutput(BaseModel):

    intent: str = Field(
        description="""
Possible intents:

investment_analysis
news
finance
comparison
risk_analysis
report
"""
    )

    companies: list[str] = Field(
        description="List of companies mentioned by the user."
    )

    confidence: float = Field(
        description="Confidence between 0 and 1"
    )