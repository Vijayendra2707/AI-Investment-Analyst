from llms.llm import llm

from models.comparison_model import ComparisonOutput
from prompts.comparison_prompt import comparison_prompt

structured_llm = llm.with_structured_output(
    ComparisonOutput
)

comparison_chain = comparison_prompt | structured_llm


def comparison_agent(state):

    companies = []

    for company in state["companies"]:

        key = company.ticker or company.input_name

        analysis = state["analysis_context"][key]

        companies.append(
            {
                "company": company.company_name,
                "ticker": company.ticker,
                "exchange": company.exchange,
                "news": analysis["news"],
                "finance": analysis["finance"],
            }
        )

    response = comparison_chain.invoke(
        {
            "companies": companies
        }
    )

    return {
        "comparison": response.model_dump()
    }