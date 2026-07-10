from state import InvestmentState


def response_agent(state: InvestmentState):

    return {
        "final_response": state["report"]
    }