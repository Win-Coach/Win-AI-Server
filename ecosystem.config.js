module.exports = {
  apps: [{
    // 1. 애플리케이션 이름
    name: 'win-ai-server',
    
    // 2. 실행할 스크립트 (가상환경의 uvicorn)
    script: './venv/bin/uvicorn',
    
    // 3. uvicorn에 전달할 인자 (안정성을 위해 --workers 1 추가)
    args: 'main:app --host 0.0.0.0 --port 8000 --workers 1',
    
    // 4. 스크립트를 실행할 인터프리터 (가상환경의 python)
    interpreter: './venv/bin/python',
    
    // 5. 실행 모드를 'cluster'로 변경 (가장 중요한 변경점)
    exec_mode: 'cluster',
    instances: 1
  }]
};
