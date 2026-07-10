from tools.company_resolver import search_companies

from models.company_model import Company
from models.resolver_model import ResolverOutput
from prompts.resolver_prompt import resolver_prompt

from state import InvestmentState
from llms.llm import llm

structured_llm = llm.with_structured_output(
    ResolverOutput
)

resolver_chain = resolver_prompt | structured_llm


def resolver_agent(state: InvestmentState):

    resolved = []

    for user_company in state["user_companies"]:

        candidates = search_companies(user_company)

        # -----------------------------
        # No candidates found
        # -----------------------------

        if not candidates:

            resolved.append(

                Company(

                    input_name=user_company,

                    company_name=user_company,

                    ticker=None,

                    exchange="Unknown",

                    is_public=False
                )
            )

            continue

        # -----------------------------
        # Ask LLM to choose
        # -----------------------------

        response = resolver_chain.invoke(
            {
                "query": user_company,
                "companies": candidates
            }
        )

        # -----------------------------
        # Validate LLM choice
        # -----------------------------

        selected_company = None

        for candidate in candidates:

            if candidate["ticker"] == response.ticker:

                selected_company = candidate
                break

        # -----------------------------
        # Fallback
        # -----------------------------

        if selected_company is None:

            selected_company = candidates[0]

        # -----------------------------
        # Build Company ONLY from API data
        # -----------------------------

        resolved.append(

            Company(

                input_name=user_company,

                company_name=selected_company["company_name"],

                ticker=selected_company["ticker"],

                exchange=selected_company["exchange"],

                is_public=True

            )

        )

    return {

        "companies": resolved

    }