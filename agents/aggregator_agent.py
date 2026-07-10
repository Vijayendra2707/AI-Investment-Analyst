from state import InvestmentState


def aggregator_agent(state: InvestmentState):

    context = {}

    for company in state["companies"]:

        key = company.ticker or company.input_name

        context[key] = {
            "news": state["news"][key],
            "finance": state["finance"][key],
        }

    return {
        "analysis_context": context
    }