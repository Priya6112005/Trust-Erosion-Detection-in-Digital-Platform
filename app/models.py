from pydantic import BaseModel

class SessionData(BaseModel):
    text: str
    abandonment: int
    policy_checks: int
    hesitation_time: int
    messages_count: int
    dispute_flag: int