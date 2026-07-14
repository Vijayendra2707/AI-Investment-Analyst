from enum import Enum


class ConversationAction(str, Enum):

    REPLACE = "replace"

    KEEP = "keep"

    MERGE = "merge"

    REMOVE = "remove"

    RESET = "reset"