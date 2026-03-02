# 콘텐츠 업데이트 스킬

기존 소구 포인트나 슬라이드 콘텐츠를 업데이트합니다.

## 사용법
`/update-content [카테고리] [변경내용]`

## 동작
1. `docs/analysis/문서분석_전체요약.md` 참조하여 현재 소구 포인트 파악
2. 변경/추가 내용을 해당 카테고리에 반영
3. `docs/content/` 내 **Ver.A/B 양쪽 모두** 슬라이드 원고 업데이트
   - `슬라이드_세부내용_VerA_비주얼.md`
   - `슬라이드_세부내용_VerB_텍스트상세.md`
4. 변경 이력을 `docs/worklog.md`에 기록

## 카테고리
| 카테고리 | 설명 | 관련 슬라이드 |
|----------|------|--------------|
| market | 시장 기회/데이터 | 3-7장 |
| business-model | 비즈니스 모델/수익 | 15-17장 |
| technology | 핵심 기술 (AI, 분산처리) | 8-14장 |
| traction | 성과/레퍼런스 | 18-20장 |
| finance | 재무/투자 | 21-23장 |
| team | 팀/회사 | 24장 |
| esg | ESG 경영 | 해당 슬라이드 |
| device | 디바이스 라인업 | 해당 슬라이드 |

## 중요 규칙
- Ver.A/B **내용은 반드시 동일** (표현 방식만 다름)
- 시장 데이터 업데이트 시 `docs/references/market_data.md`도 갱신
- `.claude/rules/korean-content.md` 용어 통일 준수
- 변경 후 `git diff`로 양쪽 버전 일관성 확인

## 연계 스킬
- `/analyze-doc` — 새 문서에서 소구 포인트 추출
- `/build-deck` — 업데이트된 콘텐츠로 PPTX 재빌드
- `/design-review` — 빌드 후 디자인 품질 검증
