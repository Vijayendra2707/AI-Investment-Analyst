from graphs.master_graph import master_graph
from models.conversation_model import ConversationContext

def main():
    thread_id = "demo-user"
    while True:

        query = input("\nAsk me anything (type 'exit' to quit): ")

        if query.lower() == "exit":
            break
        
        config = {
            "configurable": {
                "thread_id": thread_id
            }
        }

        result = master_graph.invoke(
            {
                "query": query,

                "intent": "",
                "confidence": 0.0,
                "workflow": None,

                "conversation": ConversationContext(),

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