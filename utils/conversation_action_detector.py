from models.conversation_action_model import ConversationAction


def detect_conversation_action(
    query: str,
    current_companies: list,
    user_companies: list[str],
):

    q = query.lower().strip()

    # -------------------------
    # RESET
    # -------------------------

    if any(
        phrase in q
        for phrase in [
            "reset",
            "start over",
            "clear conversation",
            "clear this conversation",
            "forget everything",
        ]
    ):

        return ConversationAction.RESET

    # -------------------------
    # REMOVE
    # -------------------------

    if any(
        phrase in q
        for phrase in [
            "remove",
            "delete",
            "forget",
            "exclude",
        ]
    ):

        return ConversationAction.REMOVE

    # -------------------------
    # KEEP
    # -------------------------

    if len(user_companies) == 0:

        return ConversationAction.KEEP

    # -------------------------
    # MERGE
    # -------------------------

    if len(current_companies) > 0:

        if any(
            phrase in q
            for phrase in [
                "compare with",
                "also compare",
                "add",
                "include",
                "along with",
                "against",
            ]
        ):

            return ConversationAction.MERGE

    # -------------------------
    # REPLACE
    # -------------------------

    return ConversationAction.REPLACE