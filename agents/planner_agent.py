from llms.llm import llm

from prompts.planner_prompt import planner_prompt
from models.planner_model import PlannerOutput

structured_llm = llm.with_structured_output(
    PlannerOutput
)

planner_chain = planner_prompt | structured_llm


def planner_agent(state):

    # ----------------------------------
    # Current conversation companies
    # ----------------------------------

    current_companies = [

        company.input_name

        for company in state["conversation"].companies

    ]

    # ----------------------------------
    # Planner
    # ----------------------------------

    response = planner_chain.invoke(

        {
            "intent": state["workflow"].value,

            "query": state["query"],

            "current_companies": current_companies,
        }

    )

    # ----------------------------------
    # Debug
    # ----------------------------------

    print("=" * 80)
    print("PLANNER")

    print("Intent:")
    print(state["workflow"])

    print("\nQuery:")
    print(state["query"])

    print("\nCurrent Companies:")
    print(current_companies)

    print("\nPlanner Output:")
    print(response)

    print("=" * 80)

    return {

        "workflow": response.workflow,

    }