module.exports = {
  apps: [{
    // 1. PM2에 표시될 애플리케이션 이름
    name: 'win-ai-server',
    
    // 2. 실행할 스크립트 (가상환경의 uvicorn)
    script: './venv/bin/uvicorn',
    
    // 3. uvicorn에 전달할 인자들
    args: 'main:app --host 0.0.0.0 --port 8000',
    
    // 4. 스크립트를 실행할 인터프리터 (가상환경의 python)
    interpreter: './venv/bin/python',
    
    // 5. PM2와 Uvicorn의 충돌을 방지하는 설정 (중요!)
    exec_mode: 'fork',
    fork: false
  }]
};
