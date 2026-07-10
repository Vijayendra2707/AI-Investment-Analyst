from graphs.workflows.investment_graph import investment_graph
from graphs.workflows.news_graph import news_graph
from graphs.workflows.finance_graph import finance_graph
from graphs.workflows.news_finance_graph import news_finance_graph
from graphs.workflows.comparison_graph import comparison_graph


def investment_node(state):
    return investment_graph.invoke(state)


def comparison_node(state):
    return comparison_graph.invoke(state)


def news_node(state):
    return news_graph.invoke(state)


def finance_node(state):
    return finance_graph.invoke(state)


def news_finance_node(state):
    return news_finance_graph.invoke(state)