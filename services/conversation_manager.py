from models.conversation_model import ConversationContext


class ConversationManager:

    @staticmethod
    def load(self, state) -> ConversationContext:

        return state["conversation"]

    @staticmethod
    def save(self, state, conversation: ConversationContext):

        state["conversation"] = conversation

        return state