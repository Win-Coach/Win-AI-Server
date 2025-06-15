from fastapi import FastAPI
from dotenv import load_dotenv

# 애플리케이션 시작 시 .env 파일에서 환경 변수를 로드합니다.
# 이 코드가 다른 import 보다 먼저 실행되도록 상단에 위치시키는 것이 좋습니다.
load_dotenv()

# .env 로드 후에 라우터를 임포트해야, 라우터 내부에서 환경 변수를 사용할 수 있습니다.
from app.routes import analyze
from app.routes import chat as chat_router 

# --- 바로 이 부분이 중요합니다! ---
# uvicorn이 찾는 'app' 변수를 여기서 생성합니다.
app = FastAPI(
    title="Win-AI-Server",
    description="데이터 분석 및 챗봇 기능을 제공하는 AI 서버입니다.",
    version="1.0.0"
)
# -----------------------------------

# 라우터 등록
# prefix="/api" 를 사용해 모든 경로 앞에 /api를 붙여줍니다.
app.include_router(analyze.router, prefix="/api", tags=["Analysis"])
app.include_router(chat_router.router, prefix="/api", tags=["Chatbot"]) 

@app.get("/", tags=["Root"])
def read_root():
    """
    서버의 루트 경로. 서버가 정상적으로 동작하는지 확인하는 용도입니다.
    """
    return {"message": "Welcome to Win-AI-Server"}

