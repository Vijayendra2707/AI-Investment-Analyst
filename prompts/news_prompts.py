from langchain_core.prompts import ChatPromptTemplate

news_prompt = ChatPromptTemplate.from_template("""
You are an expert financial news analyst.

Analyze the company: {company}

Here are the latest search results:

{search_results}

Using ONLY the information above:

1. Summarize the latest news.
2. Explain why it matters to investors.
3. Mention any opportunities.
4. Mention any risks.

Keep the response under 250 words.
""")