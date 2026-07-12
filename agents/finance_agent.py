from llms.llm import llm

from prompts.finance_prompt import finance_prompt
from models.finance_model import FinanceOutput

from tools.finance_tool import get_financial_data
from utils.retry import invoke_with_retry

structured_llm = llm.with_structured_output(
    FinanceOutput
)

finance_chain = finance_prompt | structured_llm


def finance_agent(state):

    finance_results = {}

    # ----------------------------------
    # No companies
    # ----------------------------------

    if not state["companies"]:

        return {
            "finance": {}
        }

    # ----------------------------------
    # Process each company
    # ----------------------------------

    for company in state["companies"]:

        # ----------------------------------
        # Private company
        # ----------------------------------

        if not company.is_public or company.ticker is None:

            finance_results[company.key] = {

                "company_name": company.company_name,

                "summary":
                "Financial data unavailable because the company is not publicly listed."

            }

            continue

        # ----------------------------------
        # Fetch financial data
        # ----------------------------------

        financial_data = get_financial_data(
            company.ticker
        )

        if not financial_data:

            finance_results[company.key] = {

                "company_name": company.company_name,

                "summary":
                "Financial data could not be retrieved."

            }

            continue

        # ----------------------------------
        # LLM Summary
        # ----------------------------------

        try:

            response = invoke_with_retry(

                finance_chain,

                {

                    "company": company.company_name,

                    "financial_data": financial_data

                }

            )

            finance_results[company.key] = response.model_dump()

        except Exception as e:

            finance_results[company.key] = {

                "company_name": company.company_name,

                "summary": f"Finance analysis failed: {str(e)}"

            }

    # ----------------------------------
    # Return
    # ----------------------------------

    return {

        "finance": finance_results

    }