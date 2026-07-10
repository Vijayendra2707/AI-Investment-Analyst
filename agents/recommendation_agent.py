from llms.llm import llm

from prompts.recommendation_prompt import recommendation_prompt
from models.recommendation_model import RecommendationOutput

structured_llm = llm.with_structured_output(RecommendationOutput)

recommendation_chain = recommendation_prompt | structured_llm


def recommendation_agent(state):

    recommendation_results = {}

    for company in state["companies"]:

        key = company.ticker or company.input_name
        analysis = state["analysis_context"][key]

        response = recommendation_chain.invoke(
            {
                "company": company.company_name,
                "news": analysis["news"],
                "finance": analysis["finance"],
                "risk": state["risks"][key],
            }
        )

        recommendation_results[key] = response.model_dump()

    return {
        "recommendation": recommendation_results
    }