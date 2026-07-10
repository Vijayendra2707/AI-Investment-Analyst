from langgraph.graph import StateGraph, START, END

from state import InvestmentState

from agents.news_agent import news_agent
from agents.finance_agent import finance_agent
from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent
from agents.report_agent import report_agent
from agents.aggregator_agent import aggregator_agent

builder = StateGraph(InvestmentState)

builder.add_node("NewsAgent", news_agent)
builder.add_node("FinanceAgent", finance_agent)
builder.add_node("AggregatorAgent",aggregator_agent)
builder.add_node("RiskAgent", risk_agent)
builder.add_node("RecommendationAgent", recommendation_agent)
builder.add_node("ReportAgent", report_agent)

# Run News and Finance in parallel
builder.add_edge(START, "NewsAgent")
builder.add_edge(START, "FinanceAgent")

# Wait for BOTH to finish
builder.add_edge("NewsAgent", "AggregatorAgent")
builder.add_edge("FinanceAgent", "AggregatorAgent")
builder.add_edge("AggregatorAgent","RiskAgent")

builder.add_edge("RiskAgent", "RecommendationAgent")
builder.add_edge("RecommendationAgent", "ReportAgent")
builder.add_edge("ReportAgent", END)

investment_graph = builder.compile()