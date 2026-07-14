from langchain_core.prompts import ChatPromptTemplate

intent_prompt = ChatPromptTemplate.from_template("""
Extract:

- intent
- companies
- confidence

Query:
{query}

Rules:

- Extract ONLY company names explicitly mentioned.
- Never infer or replace company names.
- If no company is mentioned return [].

Return ONLY the structured output.
""")