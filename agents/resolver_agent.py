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


def build_company(
    user_company: str,
    company: dict
) -> Company:

    return Company(

        input_name=user_company,

        company_name=company["company_name"],

        ticker=company["ticker"],

        exchange=company["exchange"],

        is_public=True

    )


def build_private_company(
    user_company: str
) -> Company:

    return Company(

        input_name=user_company,

        company_name=user_company,

        ticker=None,

        exchange="Unknown",

        is_public=False

    )


def choose_company(
    user_company: str,
    candidates: list[dict]
) -> dict:

    response = resolver_chain.invoke(

        {
            "query": user_company,
            "companies": candidates
        }

    )

    for candidate in candidates:

        if candidate["ticker"] == response.ticker:

            return candidate

    # Fallback if LLM selects something invalid
    return candidates[0]


def resolve_company(
    user_company: str
) -> Company:

    candidates = search_companies(user_company)

    # No public company found
    if not candidates:

        return build_private_company(user_company)

    # Let the LLM choose
    selected_company = choose_company(
        user_company,
        candidates
    )

    # Build Company model
    return build_company(
        user_company,
        selected_company
    )


def resolver_agent(state: InvestmentState):

    resolved_companies = []

    for user_company in state["user_companies"]:

        company = resolve_company(
            user_company
        )

        resolved_companies.append(company)

    return {

        "companies": resolved_companies

    }