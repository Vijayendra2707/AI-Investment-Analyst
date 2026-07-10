from llms.llm import llm

from prompts.finance_prompt import finance_prompt
from models.finance_model import FinanceOutput

from tools.finance_tool import get_financial_data

structured_llm = llm.with_structured_output(FinanceOutput)

finance_chain = finance_prompt | structured_llm


def finance_agent(state):

    finance_results = {}

    for company in state["companies"]:

        # Skip private companies
        if not company.is_public or company.ticker is None:
            finance_results[company.input_name] = {
                "company_name": company.company_name,
                "summary": "Financial data unavailable because the company is not publicly listed."
            }
            continue

        financial_data = get_financial_data(company.ticker)

        response = finance_chain.invoke(
            {
                "company": company.company_name,
                "financial_data": financial_data
            }
        )

        finance_results[company.ticker] = response.model_dump()

    return {
        "finance": finance_results
    }