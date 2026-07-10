from langchain_core.prompts import ChatPromptTemplate

finance_prompt = ChatPromptTemplate.from_template("""
You are a senior equity research analyst.

Analyze the following financial information.

Company:
{company}

Financial Data:

{financial_data}

Write a professional report containing:

1. Financial Health
2. Growth Potential
3. Profitability
4. Valuation
5. Strengths
6. Weaknesses

Do not invent numbers.

Base your analysis ONLY on the supplied financial data.
""")