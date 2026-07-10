from langchain_core.prompts import ChatPromptTemplate

comparison_prompt = ChatPromptTemplate.from_template("""
You are a Senior Equity Research Analyst.

Compare the following companies using ONLY the supplied information.

{companies}

For every company consider:

- Recent News
- Financial Health
- Growth Potential
- Competitive Position

Populate the structured output with:

- executive_summary
- financial_comparison
- news_comparison
- strengths
- weaknesses
- winner
- recommendation
- confidence
- conclusion

Be objective.

Return ONLY the structured output.
""")