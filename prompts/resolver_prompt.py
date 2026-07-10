from langchain_core.prompts import ChatPromptTemplate

resolver_prompt = ChatPromptTemplate.from_template("""
You are an expert stock market entity resolver.

The user searched for:

{query}

Below are the candidate companies returned from the financial API:

{companies}

Choose the single best matching company.

Rules:
- Choose ONLY from the provided candidates.
- Prefer publicly traded companies.
- Ignore ETFs, Forex pairs, cryptocurrencies, and mutual funds.
- Prefer NASDAQ/NYSE for US companies.
- Prefer NSE/BSE for Indian companies.

Return ONLY the ticker of the selected company and a confidence score.
""")