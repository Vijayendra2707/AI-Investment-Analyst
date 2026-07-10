from pydantic import BaseModel, Field

from models.company_model import Company
from models.workflow import Workflow


class ConversationContext(BaseModel):

    # Companies currently being discussed
    companies: list[Company] = Field(
        default_factory=list
    )

    # Previous workflow executed
    last_workflow: Workflow | None = None

    # Last user query
    last_query: str = ""

    # Last generated report
    last_report: dict = Field(
        default_factory=dict
    )

    # Last comparison result
    last_comparison: dict = Field(
        default_factory=dict
    )