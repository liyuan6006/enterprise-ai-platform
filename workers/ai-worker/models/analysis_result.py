from pydantic import BaseModel

class AnalysisResult(BaseModel):

    fraud_detected: bool

    risk_level: str

    policy_result: str

    ai_reasoning: str