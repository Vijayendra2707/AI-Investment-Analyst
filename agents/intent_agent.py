from llms.llm import llm

from prompts.intent_prompt import intent_prompt
from models.intent_model import IntentOutput

from utils.intent_rules import detect_workflow

structured_llm = llm.with_structured_output(IntentOutput)

intent_chain = intent_prompt | structured_llm


def intent_agent(state):

    query = state["query"]

    workflow = detect_workflow(query)

    response = intent_chain.invoke(
        {
            "query": query
        }
    )

    if workflow is not None:
        response.intent = workflow
        response.confidence = 1.0

    print("=" * 80)
    print("RAW LLM RESPONSE")
    print(response)
    print("=" * 80)

    # print("=" * 80)
    # print("INTENT")
    # print("Query:", query)
    # print("Workflow:", response.intent)
    # print("Companies:", response.companies)
    # print("=" * 80)

    return {

        "workflow": response.intent,

        "confidence": response.confidence,

        "user_companies": response.companies

    }