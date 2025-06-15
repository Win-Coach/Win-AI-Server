module.exports = {
  apps: [{
    // 1. 애플리케이션 이름
    name: 'win-ai-server',
    
    // 2. 실행할 스크립트 (Gunicorn을 실행)
    script: './venv/bin/gunicorn',
    
    // 3. Gunicorn에 전달할 설정값
    // -w 1 : 워커(일꾼) 1개 사용
    // -k uvicorn.workers.UvicornWorker : Uvicorn을 일꾼으로 사용
    // main:app : 실행할 FastAPI 앱
    // --bind 0.0.0.0:8000 : 접속 주소와 포트
    args: '-w 1 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000',
    
    // Gunicorn은 파이썬 프로그램이므로, PM2의 interpreter 설정이 필요 없습니다.
    // PM2는 Gunicorn을 직접 실행하고, Gunicorn이 내부적으로 파이썬을 올바르게 사용합니다.
  }]
};
