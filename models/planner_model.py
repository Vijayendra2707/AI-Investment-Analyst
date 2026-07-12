from pydantic import BaseModel

from models.workflow import Workflow


class PlannerOutput(BaseModel):

    workflow: Workflow
