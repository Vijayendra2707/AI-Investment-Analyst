from llms.llm import llm

from prompts.news_prompts import news_prompt
from models.news_model import NewsOutput

from tools.search_tool import search_news
from utils.retry import invoke_with_retry

structured_llm = llm.with_structured_output(
    NewsOutput
)

news_chain = news_prompt | structured_llm


def news_agent(state):

    news_results = {}

    # ----------------------------------
    # No companies
    # ----------------------------------

    if not state["companies"]:

        return {
            "news": {}
        }

    # ----------------------------------
    # Process each company
    # ----------------------------------

    for company in state["companies"]:

        # ----------------------------------
        # Search News
        # ----------------------------------

        articles = search_news(
            company.company_name
        )

        if not articles:

            news_results[company.key] = {

                "company_name": company.company_name,

                "summary":
                "No recent news could be found."

            }

            continue

        # ----------------------------------
        # LLM Summary
        # ----------------------------------

        try:

            response = invoke_with_retry(

                news_chain,

                {

                    "company": company.company_name,

                    "search_results": articles

                }

            )

            news_results[company.key] = response.model_dump()

        except Exception as e:

            news_results[company.key] = {

                "company_name": company.company_name,

                "summary": f"News analysis failed: {str(e)}"

            }

    # ----------------------------------
    # Return
    # ----------------------------------

    return {

        "news": news_results

    }