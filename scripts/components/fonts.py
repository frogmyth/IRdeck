"""AIsirius 폰트 설정 및 유틸리티.

CEO 프레젠테이션 분석 기반:
- 한글 메인: 에스코어 드림 → 맑은 고딕 폴백
- 영문 메인: Arial
- 본문 라이트: 에스코어 드림 3 Light
"""
from pptx.util import Pt
from pptx.oxml.ns import qn
from lxml import etree


# ── 폰트 역할 정의 ────────────────────────────────────
FONT_ROLES = {
    # Version 공통
    "main_heading": {
        "ea": "에스코어 드림",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(40),
        "bold": True,
    },
    "section_header": {
        "ea": "에스코어 드림",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(28),
        "bold": True,
    },
    "subtitle": {
        "ea": "에스코어 드림",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(22),
        "bold": True,
    },
    "header_english": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(14),
        "bold": False,
    },
    # Version A 전용
    "body_a": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(18),
        "bold": False,
    },
    "body_a_bold": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(18),
        "bold": True,
    },
    "keyword_a": {
        "ea": "에스코어 드림",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(24),
        "bold": True,
    },
    # Version B 전용
    "body_b": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(14),
        "bold": True,
    },
    "body_b_normal": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(14),
        "bold": False,
    },
    "quote_b": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(13),
        "bold": False,
    },
    # 공통 소형
    "small_label": {
        "ea": "에스코어 드림 3 Light",
        "ea_fallback": "맑은 고딕",
        "latin": "Calibri",
        "size": Pt(11),
        "bold": False,
    },
    "source_text": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Calibri",
        "size": Pt(9),
        "bold": False,
    },
    "slide_number": {
        "ea": "맑은 고딕",
        "ea_fallback": "맑은 고딕",
        "latin": "Arial",
        "size": Pt(10),
        "bold": False,
    },
    # 로고
    "logo_ai": {
        "ea": "Arial",
        "ea_fallback": "Arial",
        "latin": "Arial",
        "size": Pt(18),
        "bold": True,
    },
    "logo_sirius": {
        "ea": "Arial",
        "ea_fallback": "Arial",
        "latin": "Arial",
        "size": Pt(18),
        "bold": True,
    },
}


def apply_font(run, role, override_size=None, override_bold=None, color=None):
    """폰트 역할을 run에 적용.

    - East Asian / Latin 폰트를 XML 수준에서 동시 설정
    - 크기, 볼드, 색상 적용

    Args:
        run: pptx.text.run._Run 객체
        role: FONT_ROLES 키 (str)
        override_size: 크기 오버라이드 (Pt 값, optional)
        override_bold: 볼드 오버라이드 (bool, optional)
        color: RGBColor 오버라이드 (optional)
    """
    cfg = FONT_ROLES[role]

    # 기본 속성
    run.font.size = override_size or cfg["size"]
    run.font.bold = override_bold if override_bold is not None else cfg["bold"]

    if color:
        run.font.color.rgb = color

    # XML 수준에서 East Asian + Latin 폰트 설정
    rpr = run._r.get_or_add_rPr()

    # Latin 폰트
    latin_elem = rpr.find(qn("a:latin"))
    if latin_elem is None:
        latin_elem = etree.SubElement(rpr, qn("a:latin"))
    latin_elem.set("typeface", cfg["latin"])

    # East Asian 폰트
    ea_elem = rpr.find(qn("a:ea"))
    if ea_elem is None:
        ea_elem = etree.SubElement(rpr, qn("a:ea"))
    ea_elem.set("typeface", cfg["ea"])

    # python-pptx의 font.name도 설정 (Latin 기준)
    run.font.name = cfg["latin"]
