from llms.llm import llm

from prompts.risk_prompt import risk_prompt
from models.risk_model import RiskOutput

from utils.retry import invoke_with_retry

structured_llm = llm.with_structured_output(
    RiskOutput
)

risk_chain = risk_prompt | structured_llm


def risk_agent(state):

    risk_results = {}

    # ----------------------------------
    # No companies
    # ----------------------------------

    if not state["companies"]:

        return {

            "risks": {}

        }

    # ----------------------------------
    # Process each company
    # ----------------------------------

    for company in state["companies"]:

        key = company.key

        context = state["analysis_context"].get(key)

        # ----------------------------------
        # Missing analysis context
        # ----------------------------------

        if context is None:

            risk_results[key] = {

                "company_name": company.company_name,

                "summary":
                "Risk analysis unavailable because prerequisite analysis is missing."

            }

            continue

        # ----------------------------------
        # LLM Risk Analysis
        # ----------------------------------

        try:

            response = invoke_with_retry(

                risk_chain,

                {

                    "company": company.company_name,

                    "news": context.get("news"),

                    "finance": context.get("finance"),

                }

            )

            risk_results[key] = response.model_dump()

        except Exception as e:

            risk_results[key] = {

                "company_name": company.company_name,

                "summary": f"Risk analysis failed: {str(e)}"

            }

    # ----------------------------------
    # Return
    # ----------------------------------

    return {

        "risks": risk_results

    }