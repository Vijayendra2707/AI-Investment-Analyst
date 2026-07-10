from llms.llm import llm

from prompts.news_prompts import news_prompt

from models.news_model import NewsOutput

from tools.search_tool import search_news


structured_llm = llm.with_structured_output(
    NewsOutput
)

news_chain = news_prompt | structured_llm


def news_agent(state):

    news_results = {}

    for company in state["companies"]:

        articles = search_news(company.company_name)

        response = news_chain.invoke(
            {
                "company": company.company_name,

                "search_results": articles
            }
        )

        news_results[company.ticker or company.input_name] = response.model_dump()

    return {

        "news": news_results

    }