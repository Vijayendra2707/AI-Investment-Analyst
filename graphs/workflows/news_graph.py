from langgraph.graph import StateGraph, START, END

from state import InvestmentState
from agents.news_agent import news_agent

builder = StateGraph(InvestmentState)

builder.add_node("NewsAgent", news_agent)

builder.add_edge(START, "NewsAgent")
builder.add_edge("NewsAgent", END)

news_graph = builder.compile()