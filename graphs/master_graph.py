from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from state import InvestmentState

from agents.intent_agent import intent_agent
from agents.planner_agent import planner_agent
from agents.resolver_agent import resolver_agent
from agents.context_manager import context_manager
from routes.workflow_router import workflow_router

from graphs.subgraph_nodes import (
    investment_node,
    comparison_node,
    news_node,
    finance_node,
    news_finance_node,
)

builder = StateGraph(InvestmentState)

memory = MemorySaver()

# --------------------
# Core Agents
# --------------------

builder.add_node("IntentAgent", intent_agent)
builder.add_node("PlannerAgent", planner_agent)
builder.add_node("ContextManager",context_manager)
builder.add_node("ResolverAgent", resolver_agent)

# --------------------
# Workflow Nodes
# --------------------

builder.add_node("InvestmentGraph", investment_node)

builder.add_node("ComparisonGraph", comparison_node)

builder.add_node("NewsGraph", news_node)

builder.add_node("FinanceGraph", finance_node)

builder.add_node("NewsFinanceGraph", news_finance_node)

# --------------------
# Core Flow
# --------------------

builder.add_edge(START, "IntentAgent")

builder.add_edge("IntentAgent", "PlannerAgent")

builder.add_edge("PlannerAgent","ContextManager")
builder.add_edge("ContextManager","ResolverAgent")
# --------------------
# Routing
# --------------------

builder.add_conditional_edges(
    "ResolverAgent",
    workflow_router,
    {
        "InvestmentGraph": "InvestmentGraph",
        "ComparisonGraph": "ComparisonGraph",
        "NewsGraph": "NewsGraph",
        "FinanceGraph": "FinanceGraph",
        "NewsFinanceGraph": "NewsFinanceGraph",
    },
)

# --------------------
# Workflow Ends
# --------------------

builder.add_edge("InvestmentGraph", END)

builder.add_edge("ComparisonGraph", END)

builder.add_edge("NewsGraph", END)

builder.add_edge("FinanceGraph", END)

builder.add_edge("NewsFinanceGraph", END)

master_graph = builder.compile(
    checkpointer=memory
)