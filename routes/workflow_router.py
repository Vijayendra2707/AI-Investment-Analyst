from models.workflow import Workflow


def workflow_router(state):

    workflow = state["workflow"]

    if workflow == Workflow.INVESTMENT:
        return "InvestmentGraph"

    if workflow == Workflow.COMPARISON:
        return "ComparisonGraph"

    if workflow == Workflow.NEWS:
        return "NewsGraph"

    if workflow == Workflow.FINANCE:
        return "FinanceGraph"

    if workflow == Workflow.NEWS_FINANCE:
        return "NewsFinanceGraph"

    raise ValueError(f"Unknown workflow: {workflow}")