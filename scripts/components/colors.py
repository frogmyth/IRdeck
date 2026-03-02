"""AIsirius 브랜드 컬러 팔레트.

CEO 프레젠테이션(신세계inc_20260226.pptx) 분석 기반.
"""
from pptx.dml.color import RGBColor

# ── 기본 ──────────────────────────────────────────────
DARK_NAVY = RGBColor(0x0E, 0x1D, 0x62)        # 주 배경, 헤더바
VERY_DARK_NAVY = RGBColor(0x0B, 0x19, 0x2C)   # 어두운 텍스트
DARK_BLUE_BLACK = RGBColor(0x0E, 0x28, 0x41)  # 텍스트 변형
NAVY_002060 = RGBColor(0x00, 0x20, 0x60)      # 보조 배경

# ── 블루 계열 ─────────────────────────────────────────
STANDARD_BLUE = RGBColor(0x00, 0x70, 0xC0)    # 본문 강조
BRIGHT_BLUE = RGBColor(0x00, 0xB0, 0xF0)      # 하이라이트
MEDIUM_BLUE = RGBColor(0x0F, 0x9E, 0xD5)      # 보조 블루

# ── 브랜드 포인트 ─────────────────────────────────────
BRAND_CYAN = RGBColor(0x32, 0xED, 0xF6)       # 로고 "AI" 색상
TEAL = RGBColor(0x24, 0xC9, 0xD2)             # 강조 포인트

# ── 그린/레드 ─────────────────────────────────────────
LIME_GREEN = RGBColor(0x85, 0xC5, 0x3E)       # 긍정 지표
LIME_GREEN_ALT = RGBColor(0x92, 0xD0, 0x50)   # 긍정 지표 (밝은)
RED = RGBColor(0xFF, 0x00, 0x00)              # 경고 (최소 사용)

# ── 뉴트럴 ────────────────────────────────────────────
MUTED_TEAL = RGBColor(0x46, 0x78, 0x86)       # 보조 텍스트
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0x00, 0x00, 0x00)
LIGHT_GRAY = RGBColor(0xF2, 0xF2, 0xF2)       # 밝은 배경
PALE_BLUE = RGBColor(0xDC, 0xEA, 0xF7)        # 연한 파란 배경
DARK_GRAY = RGBColor(0x58, 0x58, 0x58)

# ── 유틸 ──────────────────────────────────────────────
# 차트 시리즈 색상 (최대 6개 시리즈)
CHART_SERIES = [DARK_NAVY, STANDARD_BLUE, BRAND_CYAN, LIME_GREEN, MEDIUM_BLUE, TEAL]

# 푸터 3색 바 (좌→우)
FOOTER_BAR_COLORS = [DARK_NAVY, STANDARD_BLUE, BRAND_CYAN]

# 테이블 헤더/바디 색상
TABLE_HEADER_BG = DARK_NAVY
TABLE_HEADER_FG = WHITE
TABLE_ALT_ROW = PALE_BLUE
TABLE_BODY_FG = VERY_DARK_NAVY
