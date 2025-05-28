from fastapi import FastAPI
from app.routes import analyze

app = FastAPI()

# 라우터 등록
app.include_router(analyze.router)


#uvicorn main:app --reload
