from pydantic import BaseModel

from models.workflow import Workflow
from models.conversation_action_model import ConversationAction


class PlannerOutput(BaseModel):

    workflow: Workflow