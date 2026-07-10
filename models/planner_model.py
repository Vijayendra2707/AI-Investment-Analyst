from pydantic import BaseModel, Field
from models.workflow import Workflow


class PlannerOutput(BaseModel):

    workflow: Workflow = Field(
        description="Workflow selected for this query."
    )
