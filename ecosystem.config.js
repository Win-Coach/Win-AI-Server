module.exports = {
  apps: [{
    // 1. 애플리케이션 이름
    name: 'win-ai-server',
    
    // 2. PM2가 실행할 프로그램은 'python' 입니다.
    script: './venv/bin/python',
    
    // 3. 'python' 프로그램에 전달할 인자들입니다.
    // '-m gunicorn'은 gunicorn 모듈을 실행하라는 의미입니다.
    args: '-m gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000',
  }]
};
