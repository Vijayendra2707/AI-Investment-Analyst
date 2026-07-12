from llms.llm import llm

from models.comparison_model import ComparisonOutput
from prompts.comparison_prompt import comparison_prompt

from utils.retry import invoke_with_retry

structured_llm = llm.with_structured_output(
    ComparisonOutput
)

comparison_chain = comparison_prompt | structured_llm


def comparison_agent(state):

    comparison_data = []

    # ----------------------------------
    # Need at least two companies
    # ----------------------------------

    if len(state["companies"]) < 2:

        return {

            "comparison": {}

        }

    # ----------------------------------
    # Build comparison context
    # ----------------------------------

    for company in state["companies"]:

        key = company.key

        analysis = state["analysis_context"].get(key)

        if analysis is None:

            continue

        comparison_data.append(

            {

                "company": company.company_name,

                "ticker": company.ticker,

                "exchange": company.exchange,

                "news": analysis.get("news"),

                "finance": analysis.get("finance"),

            }

        )

    # ----------------------------------
    # Not enough valid companies
    # ----------------------------------

    if len(comparison_data) < 2:

        return {

            "comparison": {}

        }

    # ----------------------------------
    # LLM Comparison
    # ----------------------------------

    try:

        response = invoke_with_retry(

            comparison_chain,

            {

                "companies": comparison_data

            }

        )

        return {

            "comparison": response.model_dump()

        }

    except Exception as e:

        return {

            "comparison": {

                "error": str(e)

            }

        }