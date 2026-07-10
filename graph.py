from state import InvestmentState

from agents.intent_agent import intent_agent
from agents.planner_agent import planner_agent
from agents.resolver_agent import resolver_agent
from agents.news_agent import news_agent
from agents.finance_agent import finance_agent
from agents.risk_agent import risk_agent
from agents.recommendation_agent import recommendation_agent
from langgraph.graph import StateGraph, START, END

builder = StateGraph(InvestmentState)

builder.add_node("IntentAgent", intent_agent)
builder.add_node("PlannerAgent",planner_agent)
builder.add_node("ResolverAgent", resolver_agent)
builder.add_node("NewsAgent", news_agent)
builder.add_node("FinanceAgent",finance_agent)
builder.add_node("RiskAgent",risk_agent)
builder.add_node("RecommendationAgent",recommendation_agent)

builder.add_edge(START, "IntentAgent")
builder.add_edge("IntentAgent", "PlannerAgent")
builder.add_edge("PlannerAgent","ResolverAgent")
builder.add_edge("ResolverAgent", "NewsAgent")
builder.add_edge("ResolverAgent", "FinanceAgent")
builder.add_edge("FinanceAgent", "RiskAgent")
builder.add_edge("NewsAgent", "RiskAgent")
builder.add_edge("RiskAgent","RecommendationAgent")
builder.add_edge("RecommendationAgent",END)



graph = builder.compile()