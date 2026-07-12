from llms.llm import llm

from prompts.report_prompt import report_prompt
from models.report_model import ReportOutput

from utils.retry import invoke_with_retry

structured_llm = llm.with_structured_output(
    ReportOutput
)

report_chain = report_prompt | structured_llm


def report_agent(state):

    reports = {}

    # ----------------------------------
    # No companies
    # ----------------------------------

    if not state["companies"]:

        return {

            "report": {}

        }

    # ----------------------------------
    # Process each company
    # ----------------------------------

    for company in state["companies"]:

        key = company.key

        analysis = state["analysis_context"].get(key)

        risks = state["risks"].get(key)

        recommendation = state["recommendation"].get(key)

        # ----------------------------------
        # Missing prerequisite analysis
        # ----------------------------------

        if (
            analysis is None
            or risks is None
            or recommendation is None
        ):

            reports[key] = {

                "company_name": company.company_name,

                "summary":
                "Report unavailable because prerequisite analysis is missing."

            }

            continue

        # ----------------------------------
        # Generate Report
        # ----------------------------------

        try:

            response = invoke_with_retry(

                report_chain,

                {

                    "company": company.company_name,

                    "ticker": company.ticker,

                    "exchange": company.exchange,

                    "news": analysis.get("news"),

                    "finance": analysis.get("finance"),

                    "risks": risks,

                    "recommendation": recommendation,

                }

            )

            reports[key] = response.model_dump()

        except Exception as e:

            reports[key] = {

                "company_name": company.company_name,

                "summary": f"Report generation failed: {str(e)}"

            }

    # ----------------------------------
    # Return
    # ----------------------------------

    return {

        "report": reports

    }