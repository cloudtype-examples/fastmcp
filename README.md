# FastMCP Server

Python 3.12 기반 FastMCP (Model Context Protocol) 서버 with Bearer Token 인증

## 🚀 실행 방법

### 로컬 실행
```bash
pip install -r requirements.txt
python server.py
```

### Docker 실행
```bash
docker build -t fastmcp .
docker run -p 8000:8000 -e FASTMCP_AUTH_TOKEN=your-secret-token fastmcp
```

## 🔐 인증

Bearer 토큰 인증을 사용합니다:
- 환경변수: `FASTMCP_AUTH_TOKEN`
- 헤더: `Authorization: Bearer your-token`

## 📋 API 기능

### Tools
- `create_task(title, description)` - 작업 생성
- `complete_task(task_id)` - 작업 완료
- `list_tasks(completed=None)` - 작업 목록
- `health_check()` - 서버 상태

### Resources
- `tasks://all` - 모든 작업
- `tasks://pending` - 대기 작업
- `tasks://completed` - 완료 작업
- `tasks://{task_id}` - 특정 작업

### Prompts
- `task_planning(project, deadline)` - 작업 계획 프롬프트

## 🌐 환경변수

- `FASTMCP_AUTH_TOKEN` - Bearer 토큰 (선택)
- `FASTMCP_HOST` - 서버 호스트 (기본: 0.0.0.0)
- `FASTMCP_PORT` - 서버 포트 (기본: 8000)