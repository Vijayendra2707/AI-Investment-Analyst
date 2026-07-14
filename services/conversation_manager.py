from copy import deepcopy

from models.company_model import Company
from models.conversation_model import ConversationContext
from models.workflow import Workflow

from utils.company_merge import merge_companies


class ConversationManager:

    @staticmethod
    def load(state) -> ConversationContext:
        return deepcopy(state["conversation"])

    @staticmethod
    def save(conversation: ConversationContext):
        return {
            "conversation": conversation
        }

    @staticmethod
    def start_new_analysis(
        conversation: ConversationContext,
    ) -> ConversationContext:

        conversation.companies = []
        conversation.last_report = {}
        conversation.last_comparison = {}

        return conversation

    @staticmethod
    def continue_analysis(
        conversation: ConversationContext,
    ) -> ConversationContext:

        return conversation

    @staticmethod
    def extend_context(
        conversation: ConversationContext,
        companies: list[Company],
    ) -> ConversationContext:

        conversation.companies = merge_companies(
            conversation.companies,
            companies,
        )

        return conversation

    @staticmethod
    def remove_company(
        conversation: ConversationContext,
        key: str,
    ) -> ConversationContext:

        conversation.companies = [

            company

            for company in conversation.companies

            if company.key != key

        ]

        return conversation

    @staticmethod
    def reset(
        conversation: ConversationContext,
    ) -> ConversationContext:

        return ConversationContext()

    @staticmethod
    def update_query(
        conversation: ConversationContext,
        query: str,
    ) -> ConversationContext:

        conversation.last_query = query

        return conversation

    @staticmethod
    def update_workflow(
        conversation: ConversationContext,
        workflow: Workflow,
    ) -> ConversationContext:

        conversation.last_workflow = workflow

        return conversation

    @staticmethod
    def update_report(
        conversation: ConversationContext,
        report: dict,
    ) -> ConversationContext:

        conversation.last_report = report

        return conversation

    @staticmethod
    def update_comparison(
        conversation: ConversationContext,
        comparison: dict,
    ) -> ConversationContext:

        conversation.last_comparison = comparison

        return conversation