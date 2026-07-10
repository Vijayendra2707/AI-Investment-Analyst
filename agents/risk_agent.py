from llms.llm import llm

from prompts.risk_prompt import risk_prompt
from models.risk_model import RiskOutput

structured_llm = llm.with_structured_output(RiskOutput)

risk_chain = risk_prompt | structured_llm


def risk_agent(state):

    risk_results = {}

    for company in state["companies"]:

        key = company.ticker or company.input_name

        context = state["analysis_context"][key]

        response = risk_chain.invoke(
            {
                "company": company.company_name,
                "news": context["news"],
                "finance": context["finance"],
            }
        )

        risk_results[key] = response.model_dump()

    return {
        "risks": risk_results
    }