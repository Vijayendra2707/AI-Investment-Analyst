from graphs.master_graph import master_graph
from models.conversation_model import ConversationContext
from utils.conversation_action_detector import detect_conversation_action
from models.conversation_action_model import ConversationAction
from services.conversation_manager import ConversationManager

def main():
    thread_id = "demo-user"
    conversation = ConversationContext()
    
    config = {
            "configurable": {
                "thread_id": thread_id
            }
        }
    while True:

        query = input("\nAsk me anything (type 'exit' to quit): ")

        # ----------------------------------
        # Application Commands
        # ----------------------------------

        action = detect_conversation_action(
            query=query,
            current_companies=conversation.companies,
            user_companies=[]
        )

        if action == ConversationAction.RESET:

            conversation = ConversationManager.reset(conversation)

            print("\n" + "=" * 80)
            print("Conversation cleared successfully.")
            print("=" * 80)

            continue

        if query.lower() == "exit":
            break

        result = master_graph.invoke(
            {
                "query": query,

                "intent": "",
                "confidence": 0.0,
                "workflow": None,

                "conversation": conversation,
                
                "user_companies": [],
                "companies": [],

                "news": {},
                "finance": {},
                "analysis_context": {},

                "comparison": {},
                "risks": {},
                "recommendation": {},
                "report": {},
            },
            config=config
        )

        print("\n" + "=" * 80)
        print("CONVERSATION AFTER GRAPH")
        print(result["conversation"])
        print("=" * 80)
        conversation = result["conversation"]

        print("\n" + "=" * 80)
        print("WORKFLOW")
        print(result["workflow"])

        print("\n" + "=" * 80)
        print("COMPANIES")

        for company in result["companies"]:
            print(company)

        print("\n" + "=" * 80)
        print("FINAL OUTPUT")

        if result["workflow"].value == "investment":

            print(result["report"])

        elif result["workflow"].value == "comparison":
            
            print(result["comparison"])

        elif result["workflow"].value == "news":

            print(result["news"])

        elif result["workflow"].value == "finance":

            print(result["finance"])

        elif result["workflow"].value == "news_finance":

            print({
                "news": result["news"],
                "finance": result["finance"]
            })


if __name__ == "__main__":
    main()