"""슬라이드 치수, 영역 좌표, 레이아웃 타입 정의.

모든 수치는 CEO 프레젠테이션(16:9, 13.33x7.50in) 기반.
"""
from enum import Enum
from pptx.util import Inches, Emu, Pt


# ── 슬라이드 치수 ─────────────────────────────────────
SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

# ── 헤더 영역 ─────────────────────────────────────────
HEADER_BAR_LEFT = Inches(0)
HEADER_BAR_TOP = Inches(0)
HEADER_BAR_WIDTH = Inches(13.333)
HEADER_BAR_HEIGHT = Inches(0.75)

# 헤더 내 섹션 제목 위치
SECTION_TITLE_LEFT = Inches(0.5)
SECTION_TITLE_TOP = Inches(0.12)
SECTION_TITLE_WIDTH = Inches(8.0)
SECTION_TITLE_HEIGHT = Inches(0.55)

# 분리선
SEPARATOR_LEFT = Inches(0.5)
SEPARATOR_TOP = Inches(0.85)
SEPARATOR_WIDTH = Inches(12.3)

# ── 로고 위치 (우상단) ────────────────────────────────
LOGO_LEFT = Inches(11.2)
LOGO_TOP = Inches(0.15)
LOGO_WIDTH = Inches(1.8)
LOGO_HEIGHT = Inches(0.45)

# ── 콘텐츠 영역 ──────────────────────────────────────
CONTENT_LEFT = Inches(0.7)
CONTENT_TOP = Inches(1.15)
CONTENT_WIDTH = Inches(11.9)
CONTENT_HEIGHT = Inches(5.6)

# ── 푸터 영역 ─────────────────────────────────────────
FOOTER_TOP = Inches(7.15)
FOOTER_HEIGHT = Inches(0.35)
FOOTER_BAR_WIDTH = Inches(13.333 / 3)

# 슬라이드 번호 위치
SLIDE_NUM_LEFT = Inches(12.3)
SLIDE_NUM_TOP = Inches(7.15)
SLIDE_NUM_WIDTH = Inches(0.7)
SLIDE_NUM_HEIGHT = Inches(0.3)

# ── Version A 콘텐츠 분할 (이미지 60%) ────────────────
A_TEXT_LEFT = CONTENT_LEFT
A_TEXT_WIDTH = Inches(4.8)
A_IMAGE_LEFT = Inches(5.8)
A_IMAGE_WIDTH = Inches(6.8)

# ── Version B 콘텐츠 분할 (텍스트 70%) ────────────────
B_TEXT_LEFT = CONTENT_LEFT
B_TEXT_WIDTH = Inches(8.0)
B_IMAGE_LEFT = Inches(9.0)
B_IMAGE_WIDTH = Inches(3.6)

# ── 차트 영역 (슬라이드 내 3개 배치) ──────────────────
CHART_3_WIDTH = Inches(3.7)
CHART_3_HEIGHT = Inches(4.2)
CHART_3_POSITIONS = [
    (Inches(0.7), CONTENT_TOP),
    (Inches(4.8), CONTENT_TOP),
    (Inches(8.9), CONTENT_TOP),
]

# 단일 차트
CHART_SINGLE_LEFT = Inches(0.7)
CHART_SINGLE_TOP = CONTENT_TOP
CHART_SINGLE_WIDTH = Inches(7.5)
CHART_SINGLE_HEIGHT = Inches(4.8)

# ── 3단 (Three Pillar) ───────────────────────────────
PILLAR_WIDTH = Inches(3.6)
PILLAR_HEIGHT = Inches(5.0)
PILLAR_GAP = Inches(0.55)
PILLAR_POSITIONS = [
    Inches(0.7),
    Inches(0.7) + PILLAR_WIDTH + PILLAR_GAP,
    Inches(0.7) + 2 * (PILLAR_WIDTH + PILLAR_GAP),
]

# ── 타임라인 ──────────────────────────────────────────
TIMELINE_Y = Inches(3.5)  # 수평선 Y 위치
TIMELINE_LEFT = Inches(1.0)
TIMELINE_WIDTH = Inches(11.3)


# ── 레이아웃 타입 열거형 ──────────────────────────────
class LayoutType(Enum):
    TITLE_COVER = "title_cover"
    SECTION_HEADER = "section_header"
    CONTENT_IMAGE_LEFT = "content_image_left"
    CONTENT_IMAGE_RIGHT = "content_image_right"
    FULL_BLEED_IMAGE = "full_bleed_image"
    TWO_COLUMN = "two_column"
    CHART_SLIDE = "chart_slide"
    CHART_DETAILED = "chart_detailed"
    COMPARISON_TABLE = "comparison_table"
    THREE_PILLAR = "three_pillar"
    TIMELINE = "timeline"
    INFOGRAPHIC_NUMBERS = "infographic_numbers"
    TEXT_HEAVY_BULLETS = "text_heavy_bullets"
    TEXT_HEAVY_TABLE = "text_heavy_table"
    TEXT_SMALL_IMAGE = "text_small_image"
    NEWS_QUOTE = "news_quote"
    TWO_COLUMN_TEXT = "two_column_text"
    THANK_YOU = "thank_you"
    GENERIC = "generic"
