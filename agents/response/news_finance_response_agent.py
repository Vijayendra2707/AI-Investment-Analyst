from state import InvestmentState


def news_finance_response_agent(state):

    return {
        "final_response": {
            "news": state["news"],
            "finance": state["finance"]
        }
    }