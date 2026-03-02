# /sync-versions 커맨드

Ver.A와 Ver.B 콘텐츠의 일관성을 검증하고 동기화합니다.

## 사용법
```
/sync-versions check     # 차이점만 확인
/sync-versions fix       # 차이점 자동 수정
```

## 검증 항목

### 1. 콘텐츠 동일성
- 각 슬라이드의 핵심 내용(팩트, 수치, 주장)이 양 버전에서 동일한지 확인
- 시장 데이터 수치 일치 여부 (ESL, RMN, AI 시장 규모)
- 회사 정보 일치 여부 (설립일, 특허, 팀 정보)

### 2. 구조 매핑
```
Ver.A (25 slides) ↔ Ver.B (28 slides)
- Cover ↔ Cover
- Market ↔ Market (Ver.B는 더 상세 분할)
- AI Core ↔ AI Core
- ...
```

### 3. 표기 통일
참조: `.claude/rules/korean-content.md`
- 용어 통일 (ESL/EPD/RMN 등)
- 숫자 표기 일관성
- 회사명 표기 일관성

## 대상 파일
- `docs/content/슬라이드_세부내용_VerA_비주얼.md`
- `docs/content/슬라이드_세부내용_VerB_텍스트상세.md`
- `docs/references/market_data.md` (시장 데이터 원본)

## 출력
```markdown
## Version Sync Report
### 일치: N개 항목
### 불일치: N개 항목
| 항목 | Ver.A | Ver.B | 조치 |
|------|-------|-------|------|
| ESL 시장 규모 | $2.34B | $2.34B | ✅ |
| RMN 성장률 | CAGR 11% | 미기재 | ⚠️ Ver.B 추가 필요 |
```
