# FastMCP Server - Python 3.12
FROM python:3.12-slim

WORKDIR /app

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Python 환경 설정
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY server.py .

# 비루트 사용자 생성
RUN useradd -m -u 1000 fastmcp && chown -R fastmcp:fastmcp /app
USER fastmcp

# 포트 노출
EXPOSE 8000

# 환경변수
ENV FASTMCP_HOST=0.0.0.0
ENV FASTMCP_PORT=8000

# 실행
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]