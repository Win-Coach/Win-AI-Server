from fastapi import FastAPI
from app.routes import analyze  # 라우터 임포트 확인

app = FastAPI()
app.include_router(analyze.router)  # 라우터 등록 확인

@app.get("/")
def root():
    return {"message": "Hello World"}  # 루트 테스트용