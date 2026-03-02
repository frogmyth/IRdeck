# /plan-slides 커맨드

슬라이드 구조를 기획하고 콘텐츠 원고를 생성합니다.

## 사용법
```
/plan-slides [유형] [대상]
```
- 유형: ir | intro | partner | cms
- 대상: general | [회사명]

## 기획 프로세스

### 1. 대상 분석
- 청중 파악 (투자자/파트너/고객)
- 핵심 메시지 1문장 정의
- 3-5개 핵심 포인트 도출
- Call to Action 정의

### 2. 콘텐츠 계층 설계
참조: `.claude/rules/presentation-rules.md`
```
1. AI 핵심 역량 (최우선)
2. 플랫폼 통합 (RMN+ESL)
3. 시장 기회
4. 비즈니스 모델
5. 차별점 (전용 AI vs 범용 AI)
```

### 3. 슬라이드 시퀀스 설계
참조: `.agents/skills/presentation-design/SKILL.md`
- 2분 내 핵심 메시지 전달 가능한 구조
- Essential / Standard / Expandable 콘텐츠 구분
- 논리적 흐름 (문제→해법→증거→행동)

### 4. 레이아웃 매핑
각 슬라이드에 적합한 레이아웃 타입 배정:
- TITLE_COVER, TWO_COLUMN, CHART_SLIDE, THREE_PILLAR 등 18종

### 5. 원고 생성
- `docs/content/` 에 Ver.A/B 양쪽 모두 생성
- `.claude/rules/korean-content.md` 용어 규칙 준수
- 시장 데이터는 `docs/references/market_data.md` 참조

## 출력
- `docs/content/회사소개서_슬라이드구조.md` (구조)
- `docs/content/슬라이드_세부내용_Ver[A|B]_[유형].md` (원고)
