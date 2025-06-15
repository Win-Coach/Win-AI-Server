import os
from openai import AsyncOpenAI
from app.models.schemas import ChatInput

# OpenAI 비동기 클라이언트 초기화
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 챗봇의 역할과 답변 스타일을 정의하는 시스템 프롬프트 (정중한 말투로 수정)
SYSTEM_PROMPT = """
당신은 '마음코치'라는 이름을 가진 스포츠 심리 상담사입니다. 
항상 운동선수에게 용기를 주고, 스포츠 심리학에 기반하여 간결하고 명확한 조언을 해주세요.
답변은 너무 길지 않게, 실제 챗봇처럼 정중한 '해요체'를 사용하여 단답형으로 대답해주세요.
모든 답변은 한국어로 해주세요.
"""

async def get_chat_response(chat_input: ChatInput) -> str:
    """
    ChatInput 모델을 받아 LLM으로부터 답변을 생성하고 문자열로 반환합니다.
    스포츠 심리 상담사 역할을 부여하고, 답변을 간결하게 하도록 지시합니다.
    """
    try:
        # Pydantic 모델을 dict 리스트로 변환
        messages_for_api = [msg.model_dump() for msg in chat_input.messages]

        # 시스템 프롬프트를 전체 대화의 맨 앞에 추가합니다.
        # 이렇게 하면 LLM이 대화 내내 자신의 역할을 인지하게 됩니다.
        messages_with_system_prompt = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + messages_for_api

        # OpenAI ChatCompletion API 호출
        chat_completion = await client.chat.completions.create(
            messages=messages_with_system_prompt,
            model="gpt-4o",
            # 답변 길이를 제한하고 싶다면 max_tokens를 사용할 수 있습니다.
            # 예: max_tokens=150
        )
        
        assistant_response = chat_completion.choices[0].message.content
        return assistant_response

    except Exception as e:
        print(f"OpenAI API 호출 중 오류 발생: {e}")
        return "죄송합니다, 응답을 생성하는 중에 오류가 발생했습니다."
