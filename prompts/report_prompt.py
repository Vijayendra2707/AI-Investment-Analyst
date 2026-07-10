from langchain_core.prompts import ChatPromptTemplate

report_prompt = ChatPromptTemplate.from_template("""
You are a Senior Equity Research Analyst.

Using the provided information, generate a professional investment report.

Company:
{company}

Ticker:
{ticker}

Exchange:
{exchange}

Latest News:
{news}

Financial Analysis:
{finance}

Risk Analysis:
{risks}

Investment Recommendation:
{recommendation}

Populate the structured output with:

- company
- executive_summary
- news_summary
- financial_summary
- risk_summary
- recommendation
- confidence
- conclusion

Return ONLY the structured output.
""")