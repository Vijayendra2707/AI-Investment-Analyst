from llms.llm import llm

from prompts.report_prompt import report_prompt
from models.report_model import ReportOutput

structured_llm = llm.with_structured_output(
    ReportOutput
)

report_chain = report_prompt | structured_llm


def report_agent(state):

    reports = {}

    for company in state["companies"]:

        key = company.ticker or company.input_name

        analysis = state["analysis_context"][key]

        response = report_chain.invoke(
            {
                "company": company.company_name,
                "ticker": company.ticker,
                "exchange": company.exchange,

                "news": analysis["news"],

                "finance": analysis["finance"],

                "risks": state["risks"][key],   # plural

                "recommendation": state["recommendation"][key]
            }
        )

        reports[key] = response.model_dump()

    return {
        "report": reports
    }