# 보안 규칙

## 기밀 정보 관리
- `docs/credentials.md` — git에서 제외 (.gitignore)
- API 키 (Gamma, ComfyUI 등) — 환경 변수 또는 credentials.md에만 저장
- 투자 조건, 주식 현황 — `general` 버전에서 제외

## 커뮤니티 스킬 설치 시 검증
새 스킬 설치 전 반드시 확인:
1. 설치 수 확인 (50 이상 권장)
2. GitHub 소스 확인 (공개 레포, 알려진 작성자)
3. 실행 파일 존재 시 전체 코드 리뷰:
   - 외부 네트워크 호출 (requests, fetch, curl) 없음 확인
   - eval()/exec()/shell=True 없음 확인
   - 파일 삭제/환경변수 접근 확인
   - base64/난독화 코드 없음 확인
4. 프롬프트 인젝션 패턴 없음 확인

## 외부 공유 시
- 워터마크 PDF로 변환 (`scripts/watermark_pdf.py`)
- 대상사명 + 날짜 워터마크 적용
- 원본 PPTX는 직접 전달 금지 (편집 방지)

## Git 보안
- .gitignore에서 credentials.md 제외 확인
- 커밋 전 `git diff --cached`로 민감 정보 유출 확인
- force push 금지
