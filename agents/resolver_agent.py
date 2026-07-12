from tools.company_resolver import search_companies

from models.company_model import Company
from models.resolver_model import ResolverOutput
from prompts.resolver_prompt import resolver_prompt
from services.conversation_manager import ConversationManager
from utils.company_merge import merge_companies

from models.workflow import Workflow

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

    # ----------------------------------
    # Load current conversation
    # ----------------------------------

    conversation = ConversationManager.load(state)

    resolved_companies = []

    # ----------------------------------
    # Resolve companies mentioned
    # ----------------------------------

    for user_company in state["user_companies"]:

        company = resolve_company(user_company)

        resolved_companies.append(company)

    # ----------------------------------
    # Decide how to update conversation
    # ----------------------------------

    # ----------------------------------
    # Decide how to update conversation
    # ----------------------------------

    if len(resolved_companies) == 0:

        # No new companies mentioned.

        # Keep previous conversation.
        pass

    elif state["workflow"] == Workflow.COMPARISON:

        # Merge for comparison

        conversation.companies = merge_companies(
            conversation.companies,
            resolved_companies
        )

    else:

        # Replace current conversation

        conversation.companies = resolved_companies
    # ----------------------------------
    # Update conversation metadata
    # ----------------------------------

    conversation = ConversationManager.update_query(
        conversation,
        state["query"]
    )

    conversation = ConversationManager.update_workflow(
        conversation,
        state["workflow"]
    )

    # ----------------------------------
    # Return updated state
    # ----------------------------------
    return {

        "conversation": conversation,

        "companies": conversation.companies

    }

