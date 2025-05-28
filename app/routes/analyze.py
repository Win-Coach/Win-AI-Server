# routes/analyze.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AnalyzeInput(BaseModel):
    training_content: str
    feedback: str
    next_goal: str

@router.post("/analyze")
def analyze(input: AnalyzeInput):
    return {
        "good": "훈련에 대한 집중력이 매우 좋았어요!",
        "bad": "성과를 좀 더 높게 가져가야 합니다.",
        "coaching": "지금까지 꾸준하게 가져간 긍정적인 감정을 계속 이어가주세요"
    }

