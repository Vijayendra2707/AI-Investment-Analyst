from typing import Any, TypedDict
from models.company_model import Company
from models.comparison_model import ComparisonOutput
from models.news_model import NewsOutput
from models.finance_model import FinanceOutput
from models.risk_model import RiskOutput
from models.recommendation_model import RecommendationOutput
from models.report_model import ReportOutput
from models.workflow import Workflow
from models.conversation_model import ConversationContext
from models.conversation_action_model import ConversationAction

class InvestmentState(TypedDict):

    query: str

    intent: str
    confidence: float

    workflow: Workflow | None

    conversation: ConversationContext

    analysis_context: dict[str, Any]
    comparison: dict[str, ComparisonOutput]
    user_companies: list[str]

    companies: list[Company]

    news: dict[str, NewsOutput]

    finance: dict[str, FinanceOutput]

    risks: dict[str, RiskOutput]

    recommendation: dict[str, RecommendationOutput]

    report: dict[str, ReportOutput]

    final_response: dict