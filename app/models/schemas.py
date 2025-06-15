from pydantic import BaseModel, Field
from typing import List

# 하나의 메시지 단위를 정의하는 모델
class Message(BaseModel):
    role: str = Field(..., description="메시지 발신자 역할 (예: 'user', 'assistant')")
    content: str = Field(..., description="메시지 내용")

# 챗봇 API에 요청할 때 전체 대화 기록을 담는 모델
class ChatInput(BaseModel):
    messages: List[Message] = Field(..., description="전체 대화 기록 리스트")

