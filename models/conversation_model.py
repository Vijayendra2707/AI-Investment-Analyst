from pydantic import BaseModel, Field

from models.company_model import Company
from models.workflow import Workflow


class ConversationContext(BaseModel):

    # Active companies in the conversation
    companies: list[Company] = Field(default_factory=list)

    # Previous workflow
    last_workflow: Workflow | None = None

    # Previous user query
    last_query: str = ""

    # Previous report
    last_report: dict = Field(default_factory=dict)

    # Previous comparison
    last_comparison: dict = Field(default_factory=dict)