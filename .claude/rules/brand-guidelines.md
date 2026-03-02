# AIsirius 브랜드 가이드라인

## 컬러 시스템

| 역할 | 이름 | HEX | 사용처 |
|------|------|-----|--------|
| Primary | Dark Navy | `#0E1D62` | 헤더, 제목, 주요 배경 |
| Accent | Brand Cyan | `#32EDF6` | 강조, 구분선, 포인트 |
| Secondary | Standard Blue | `#0070C0` | 본문 강조, 차트 |
| Text | Dark Gray | `#333333` | 본문 텍스트 |
| Background | White | `#FFFFFF` | 슬라이드 배경 |
| Light BG | Light Gray | `#F2F2F2` | 보조 배경 |
| Success | Lime Green | `#92D050` | 긍정 지표 |
| Highlight | Gold | `#FFC000` | 핵심 수치 |

### 60-30-10 비율
- 60% White/Light Gray (배경)
- 30% Dark Navy (구조/헤더)
- 10% Brand Cyan (강조/액센트)

## 타이포그래피

| 역할 | 한글 | 영문 | 크기 | 굵기 |
|------|------|------|------|------|
| 메인 제목 | 에스코어 드림 | Arial | 36-44pt | Bold |
| 서브 제목 | 에스코어 드림 | Arial | 24-28pt | Bold |
| 본문 (Ver.A) | 맑은 고딕 | Arial | 18-20pt | Regular |
| 본문 (Ver.B) | 맑은 고딕 | Arial | 14-16pt | Regular |
| 캡션/주석 | 맑은 고딕 | Arial | 10-12pt | Regular |

### 폰트 사용 규칙
- 한글/영문 동시 사용 시 반드시 EA + Latin 폰트 모두 지정
- python-pptx에서 `apply_font()` 함수 사용 (XML 레벨 EA/Latin 설정)

## 슬라이드 규격
- 비율: 16:9 (1920×1080 / 13.333×7.5 inches)
- 여백: 좌우 0.5", 상하 0.4"
- 헤더 영역: 상단 1.0"
- 푸터 영역: 하단 0.3"

## 크롬 요소 (Chrome)
- **헤더 바**: 오각형(chevron) + 섹션명 (Dark Navy)
- **푸터 바**: 3색 가로 바 (Navy, Blue, Cyan)
- **구분선**: Cyan 수평선
- **로고**: "AI" (Cyan) + "sirius" (Navy) 텍스트 로고

## 차트/테이블 스타일
- 차트 시리즈 색상 순서: Navy → Blue → Cyan → Green → Medium Blue → Teal
- 테이블 헤더: Dark Navy 배경 + White 텍스트
- 테이블 본문: 짝수행 Light Gray, 홀수행 White
