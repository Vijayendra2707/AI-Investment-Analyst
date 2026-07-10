from langgraph.graph import StateGraph, START, END

from state import InvestmentState

from agents.news_agent import news_agent
from agents.finance_agent import finance_agent
from agents.aggregator_agent import aggregator_agent

builder = StateGraph(InvestmentState)

builder.add_node("NewsAgent", news_agent)
builder.add_node("FinanceAgent", finance_agent)
builder.add_node("AggregatorAgent", aggregator_agent)

builder.add_edge(START, "NewsAgent")
builder.add_edge(START, "FinanceAgent")

builder.add_edge("NewsAgent", "AggregatorAgent")
builder.add_edge("FinanceAgent", "AggregatorAgent")

builder.add_edge("AggregatorAgent", END)

news_finance_graph = builder.compile()