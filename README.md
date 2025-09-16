# FastMCP Server

Python FastMCP (Model Context Protocol) 서버 with Bearer Token 인증



## 실행 방법

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



## 배포하기

### 클라우드타입

1. **템플릿 선택하기** : `FastMCP`

<p align="center">
  <img src="https://raw.githubusercontent.com/cloudtype-examples/assets/refs/heads/main/screenshots/fastmcp/select.png" width="600px">
</p>



2. **배포하기**

- **Python 3.12**
- **환경변수**
  `FASTMCP_AUTH_TOKEN` : 인증에 사용할 토큰을 설정 (인증시 사용할 토큰)
- **시작 명령어**
   `uvicorn server:app --host 0.0.0.0 --port 8000`

<p align="center">
  <img src="https://raw.githubusercontent.com/cloudtype-examples/assets/refs/heads/main/screenshots/fastmcp/config.png" width="600px">
</p>


3. **접속정보 확인**

   > MCP 접속 주소 - **https://<배포된 프리뷰 도메인 주소>/mcp**

<p align="center">
  <img src="https://raw.githubusercontent.com/cloudtype-examples/assets/refs/heads/main/screenshots/fastmcp/domain.png" width="600px">
</p>


4. **업데이트**
   코드 커밋 & 푸시 후 `설정` 탭에서 `배포하기` 버튼으로 배포



#### YouTube 가이드

- [MCP 서버 배포하기 - YouTube 가이드](https://www.youtube.com/watch?v=Y3AK40FVCbw)


#### 배포자동화

- [클라우드타입 GitHub Actions 가이드](https://docs.cloudtype.io/guide/cicd/github-actions)



## 인증

Bearer 토큰 인증을 사용합니다:
- 환경변수: `FASTMCP_AUTH_TOKEN`
- 헤더: `Authorization: Bearer your-token`



## 지원 도구
- **create_task** : 작업 생성하기
- **complete_task** : 작업 완료하기
- **list_tasks** : 작업 목록 조회하기



## 환경변수

- **FASTMCP_AUTH_TOKEN** : Bearer 토큰 (**필수**)
- **FASTMCP_HOST** : 서버 호스트 (선택/기본: 0.0.0.0)
- **FASTMCP_PORT** : 서버 포트 (선택/기본: 8000)




## 활용방법

### Porter AI
- [Porter AI 에서 MCP 연결하기](https://docs.getporter.ai/ko/mcp) 
- [Slack 연동하기](https://docs.getporter.ai/ko/slack)
- [Porter AI](https://getporter.ai/)

## 문제해결

- [클라우드타입 가이드](https://docs.cloudtype.io/)
- [클라우드타입 디스코드](https://discord.gg/U7HX4BA6hu)


## License

MIT License