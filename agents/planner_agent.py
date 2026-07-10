from llms.llm import llm

from prompts.planner_prompt import planner_prompt
from models.planner_model import PlannerOutput

structured_llm = llm.with_structured_output(
    PlannerOutput
)

planner_chain = planner_prompt | structured_llm


def planner_agent(state):

    response = planner_chain.invoke(
        {
            "intent": state["intent"]
        }
    )

    return {
        "workflow": response.workflow,
        }