from llms.llm import llm

from prompts.recommendation_prompt import recommendation_prompt
from models.recommendation_model import RecommendationOutput

from utils.retry import invoke_with_retry

structured_llm = llm.with_structured_output(
    RecommendationOutput
)

recommendation_chain = recommendation_prompt | structured_llm


def recommendation_agent(state):

    recommendation_results = {}

    # ----------------------------------
    # No companies
    # ----------------------------------

    if not state["companies"]:

        return {

            "recommendation": {}

        }

    # ----------------------------------
    # Process each company
    # ----------------------------------

    for company in state["companies"]:

        key = company.key

        analysis = state["analysis_context"].get(key)
        risk = state["risks"].get(key)

        # ----------------------------------
        # Missing prerequisite analysis
        # ----------------------------------

        if analysis is None or risk is None:

            recommendation_results[key] = {

                "company_name": company.company_name,

                "summary":
                "Recommendation unavailable because prerequisite analysis is missing."

            }

            continue

        # ----------------------------------
        # LLM Recommendation
        # ----------------------------------

        try:

            response = invoke_with_retry(

                recommendation_chain,

                {

                    "company": company.company_name,

                    "news": analysis.get("news"),

                    "finance": analysis.get("finance"),

                    "risk": risk,

                }

            )

            recommendation_results[key] = response.model_dump()

        except Exception as e:

            recommendation_results[key] = {

                "company_name": company.company_name,

                "summary": f"Recommendation generation failed: {str(e)}"

            }

    # ----------------------------------
    # Return
    # ----------------------------------

    return {

        "recommendation": recommendation_results

    }