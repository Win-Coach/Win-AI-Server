from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatInput
from app.services.chatbot import get_chat_response

# --- 바로 이 부분이 중요합니다! ---
# APIRouter 인스턴스를 'router'라는 이름으로 생성합니다.
router = APIRouter()
# -----------------------------------

@router.post("/chat", summary="Get a response from the chatbot")
async def handle_chat_request(chat_input: ChatInput):
    """
    /api/chat 경로의 POST 요청을 처리합니다.
    
    - **chat_input**: 전체 대화 기록을 포함하는 요청 본문입니다.
    
    챗봇 서비스 함수를 호출하고 LLM의 응답을 클라이언트에 반환합니다.
    """
    try:
        response_text = await get_chat_response(chat_input)
        return {"response": response_text}
    except Exception as e:
        # 서비스에서 발생한 예외를 처리하고 클라이언트에게 500 에러를 보냅니다.
        raise HTTPException(status_code=500, detail=str(e))
