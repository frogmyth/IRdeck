"""슬라이드 크롬 요소: 헤더바, 푸터, 로고, 분리선.

CEO 프레젠테이션의 시각적 아이덴티티를 재현한다.
- 오각형(쉐브론) 헤더바 + 섹션 제목
- 하단 3색 직사각형 바
- 수평 분리선
- 우상단 AIsirius 로고 (AI=Cyan, sirius=Navy)
"""
from pptx.util import Inches, Pt, Emu
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

from .colors import (
    DARK_NAVY, BRAND_CYAN, STANDARD_BLUE, WHITE, MUTED_TEAL,
    FOOTER_BAR_COLORS, VERY_DARK_NAVY,
)
from .fonts import apply_font
from .layouts import (
    HEADER_BAR_LEFT, HEADER_BAR_TOP, HEADER_BAR_WIDTH, HEADER_BAR_HEIGHT,
    SECTION_TITLE_LEFT, SECTION_TITLE_TOP, SECTION_TITLE_WIDTH, SECTION_TITLE_HEIGHT,
    SEPARATOR_LEFT, SEPARATOR_TOP, SEPARATOR_WIDTH,
    LOGO_LEFT, LOGO_TOP, LOGO_WIDTH, LOGO_HEIGHT,
    FOOTER_TOP, FOOTER_HEIGHT, FOOTER_BAR_WIDTH,
    SLIDE_NUM_LEFT, SLIDE_NUM_TOP, SLIDE_NUM_WIDTH, SLIDE_NUM_HEIGHT,
    SLIDE_WIDTH,
)


def add_header_bar(slide, section_title="", section_english=""):
    """오각형(쉐브론) 헤더바를 슬라이드 상단에 추가.

    Args:
        slide: pptx Slide 객체
        section_title: 한글 섹션 제목 (예: "시장 기회")
        section_english: 영문 라벨 (예: "Marketing Opportunity")
    """
    # 헤더 배경 — 쉐브론(오각형) shape
    header = slide.shapes.add_shape(
        MSO_SHAPE.CHEVRON,
        HEADER_BAR_LEFT, HEADER_BAR_TOP,
        HEADER_BAR_WIDTH, HEADER_BAR_HEIGHT,
    )
    header.fill.solid()
    header.fill.fore_color.rgb = DARK_NAVY
    header.line.fill.background()  # 테두리 없음

    # 섹션 제목 텍스트
    if section_title or section_english:
        txbox = slide.shapes.add_textbox(
            SECTION_TITLE_LEFT, SECTION_TITLE_TOP,
            SECTION_TITLE_WIDTH, SECTION_TITLE_HEIGHT,
        )
        tf = txbox.text_frame
        tf.word_wrap = True

        # 영문 라벨 먼저 (있으면)
        if section_english:
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = f"AIsirius | {section_english}"
            apply_font(run, "header_english", color=WHITE)

        # 한글 제목 (있으면)
        if section_title:
            if section_english:
                p = tf.add_paragraph()
            else:
                p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = section_title
            apply_font(run, "section_header", override_size=Pt(20), color=WHITE)


def add_footer_bars(slide):
    """하단 3색 직사각형 바 추가."""
    for i, color in enumerate(FOOTER_BAR_COLORS):
        bar = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            Inches(i * (13.333 / 3)), FOOTER_TOP,
            FOOTER_BAR_WIDTH, FOOTER_HEIGHT,
        )
        bar.fill.solid()
        bar.fill.fore_color.rgb = color
        bar.line.fill.background()


def add_separator_line(slide):
    """헤더 아래 수평 분리선 추가."""
    connector = slide.shapes.add_connector(
        1,  # straight connector
        SEPARATOR_LEFT, SEPARATOR_TOP,
        SEPARATOR_LEFT + SEPARATOR_WIDTH, SEPARATOR_TOP,
    )
    connector.line.color.rgb = BRAND_CYAN
    connector.line.width = Pt(1.5)


def add_logo(slide):
    """우상단 AIsirius 로고 텍스트 추가.

    "AI" = Cyan (#32EDF6), "sirius" = Dark Navy (#0E1D62)
    """
    txbox = slide.shapes.add_textbox(
        LOGO_LEFT, LOGO_TOP,
        LOGO_WIDTH, LOGO_HEIGHT,
    )
    tf = txbox.text_frame
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT

    # "AI" run
    run_ai = p.add_run()
    run_ai.text = "AI"
    apply_font(run_ai, "logo_ai", color=BRAND_CYAN)

    # "sirius" run
    run_sirius = p.add_run()
    run_sirius.text = "sirius"
    apply_font(run_sirius, "logo_sirius", color=DARK_NAVY)


def add_slide_number(slide, number, total=None):
    """슬라이드 번호 추가."""
    txbox = slide.shapes.add_textbox(
        SLIDE_NUM_LEFT, SLIDE_NUM_TOP,
        SLIDE_NUM_WIDTH, SLIDE_NUM_HEIGHT,
    )
    tf = txbox.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT

    text = f"{number}" if total is None else f"{number} / {total}"
    run = p.add_run()
    run.text = text
    apply_font(run, "slide_number", color=MUTED_TEAL)


def add_full_chrome(slide, section_title="", section_english="", slide_number=None, total_slides=None):
    """크롬 요소 전체 적용 (표지/감사 슬라이드 제외 시 사용).

    Args:
        slide: pptx Slide 객체
        section_title: 한글 섹션 제목
        section_english: 영문 라벨
        slide_number: 슬라이드 번호 (int, optional)
        total_slides: 전체 슬라이드 수 (int, optional)
    """
    add_header_bar(slide, section_title, section_english)
    add_separator_line(slide)
    add_footer_bars(slide)
    add_logo(slide)
    if slide_number is not None:
        add_slide_number(slide, slide_number, total_slides)
