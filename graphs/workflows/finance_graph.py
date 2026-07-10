from langgraph.graph import StateGraph, START, END

from state import InvestmentState
from agents.finance_agent import finance_agent

builder = StateGraph(InvestmentState)

builder.add_node("FinanceAgent", finance_agent)

builder.add_edge(START, "FinanceAgent")
builder.add_edge("FinanceAgent", END)

finance_graph = builder.compile()