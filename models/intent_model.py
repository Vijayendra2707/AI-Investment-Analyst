from pydantic import BaseModel, Field

from models.workflow import Workflow


class IntentOutput(BaseModel):

    intent: Workflow = Field(
        description="""
The workflow that should execute.

Allowed values:

investment
comparison
news
finance
news_finance
"""
    )

    companies: list[str] = Field(
        default_factory=list,
        description="Companies explicitly mentioned by the user."
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1."
    )