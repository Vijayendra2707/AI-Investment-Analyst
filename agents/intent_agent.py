from llms.llm import llm

from models.intent_model import IntentOutput

from prompts.intent_prompt import intent_prompt


structured_llm = llm.with_structured_output(IntentOutput)

intent_chain = intent_prompt | structured_llm


def intent_agent(state):

    result = intent_chain.invoke(
        {
            "query": state["query"]
        }
    )
    
    return {

        "intent": result.intent,

        "confidence": result.confidence,

        "user_companies": result.companies
        
    }