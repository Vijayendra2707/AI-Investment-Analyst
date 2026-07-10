from state import InvestmentState

def skip_finance(state: InvestmentState):

    return {
        "finance":
        "Financial analysis skipped because this company is not publicly traded."
    }