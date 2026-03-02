# Pencil 디자인 스킬

Pencil MCP를 사용하여 .pen 파일에서 프레젠테이션 슬라이드를 디자인합니다.

## 사용법
`/pencil-design [슬라이드유형]`
- 유형: cover | market-data | pillars | comparison | revenue | closing | all

## 동작
1. `mcp__pencil__get_editor_state` — 현재 에디터 상태 확인
2. `mcp__pencil__get_guidelines("design-system")` — 디자인 가이드라인 로드
3. `mcp__pencil__get_style_guide_tags` + `get_style_guide` — 스타일 영감
4. `mcp__pencil__batch_design` — 슬라이드 생성 (최대 25 ops/call)
5. `mcp__pencil__get_screenshot` — 시각적 검증

## 브랜드 적용
- `.claude/rules/brand-guidelines.md` 참조
- Dark Navy `#0E1D62`, Cyan `#32EDF6`, Blue `#0070C0`
- 16:9 (1920×1080), 제목 ≥40px, 본문 ≥24px

## 레이아웃 계약 (L01-L20)
| 코드 | 용도 | 구성 |
|------|------|------|
| L01 | Cover | 로고 + 회사명 + 태그라인 |
| L02 | Section Opener | 배경 + 섹션명 |
| L07 | 3 Pillars | 3칼럼 아이콘+제목+설명 |
| L08 | Compare | 좌/우 대비 (전용 AI vs 범용 AI) |
| L13 | Revenue/Process | 단계별 프로세스 다이어그램 |
| L17 | Data + Insight | 차트 + 핵심 인사이트 텍스트 |
| L20 | Closing | CTA + 연락처 |

## 주의사항
- .pen 파일은 Pencil MCP 도구로만 접근 (Read/Grep 사용 금지)
- batch_design은 한 번에 25개 이하 operations
- 생성 후 반드시 get_screenshot으로 시각적 검증
