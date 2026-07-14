from tools.company_resolver import search_companies

from utils.conversation_action_detector import detect_conversation_action
from models.company_model import Company
from models.resolver_model import ResolverOutput
from prompts.resolver_prompt import resolver_prompt
from services.conversation_manager import ConversationManager
from utils.company_merge import merge_companies
from models.conversation_action_model import ConversationAction

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
    print("=" * 80)
    print("RESOLVER INPUT")
    print("Conversation Companies:")
    for c in state["conversation"].companies:
        print(c)

    print("User Companies:")
    print(state["user_companies"])

    print("Workflow:")
    print(state["workflow"])
    print("=" * 80)
    resolved_companies = []

    # ----------------------------------
    # Resolve companies mentioned
    # ----------------------------------

    for user_company in state["user_companies"]:

        company = resolve_company(user_company)

        resolved_companies.append(company)
    
        # ----------------------------------
    # Update conversation
    # ----------------------------------

    action = detect_conversation_action(

        query=state["query"],

        current_companies=conversation.companies,

        user_companies=state["user_companies"]

    )
    if action == ConversationAction.KEEP:

        # No change to the conversation
        pass

    elif action == ConversationAction.REPLACE:

        conversation.companies = resolved_companies

    elif action == ConversationAction.MERGE:

        conversation.companies = merge_companies(
            conversation.companies,
            resolved_companies
        )

    elif action == ConversationAction.REMOVE:

        for company in resolved_companies:

            conversation = ConversationManager.remove_company(
                conversation,
                company.key
            )

    elif action == ConversationAction.RESET:

        conversation = ConversationManager.reset(conversation)

    conversation = ConversationManager.update_query(
        conversation,
        state["query"]
    )

    conversation = ConversationManager.update_workflow(
        conversation,
        state["workflow"]
    )
    
    print("=" * 80)
    print("CONVERSATION ACTION")
    print(action)

    print("Conversation Companies:")
    for company in conversation.companies:
        print(company)

    print("=" * 80)
    # ----------------------------------
    # Return updated state
    # ----------------------------------
    return {

        "conversation": conversation,

        "companies": conversation.companies

    }

