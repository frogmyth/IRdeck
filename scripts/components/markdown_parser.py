"""마크다운 콘텐츠 파일 → SlideContent 파싱.

Version A: `슬라이드_세부내용_VerA_비주얼.md`
Version B: `슬라이드_세부내용_VerB_텍스트상세.md`
Version IR: `투자제안서_슬라이드_세부내용.md`

모든 파일은 `## Slide N. Title` 패턴으로 슬라이드를 구분한다.
"""
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from .layouts import LayoutType


@dataclass
class SlideContent:
    """파싱된 슬라이드 한 장의 내용."""
    number: int
    title: str
    layout_type: LayoutType = LayoutType.GENERIC
    layout_hint: str = ""          # 원본 레이아웃 설명
    headline: str = ""             # 메인 카피 / 헤드라인
    section_title: str = ""        # 한글 섹션 제목
    section_english: str = ""      # 영문 헤더 라벨
    body_texts: list = field(default_factory=list)    # 본문 텍스트 블록 리스트
    bullets: list = field(default_factory=list)        # 불릿 리스트 (문자열)
    tables: list = field(default_factory=list)         # 파싱된 테이블 [{header: [...], rows: [[...]]}]
    quotes: list = field(default_factory=list)         # 인용문 리스트
    chart_keys: list = field(default_factory=list)     # MARKET_DATA 키 (예: "ESL", "RMN_AD_SPEND")
    image_refs: list = field(default_factory=list)     # 이미지 참조 설명
    notes: str = ""                # 발표자 노트
    raw_text: str = ""             # 파싱 안 된 원본 텍스트


# ── 슬라이드 경계 패턴 ────────────────────────────────
_SLIDE_RE = re.compile(r"^## Slide (\d+)[\.\s]*(.+)$", re.MULTILINE)

# ── 메타 키-값 패턴 ───────────────────────────────────
_META_RE = re.compile(r"^\*\*(.+?)\*\*\s*[:：]\s*(.+)$", re.MULTILINE)

# ── 테이블 행 패턴 ────────────────────────────────────
_TABLE_ROW_RE = re.compile(r"^\|(.+)\|$")
_TABLE_SEP_RE = re.compile(r"^\|[-\s|:]+\|$")

# ── 불릿 패턴 ─────────────────────────────────────────
_BULLET_RE = re.compile(r"^[-*]\s+(.+)$")
_NUM_BULLET_RE = re.compile(r"^\d+[.)]\s+(.+)$")

# ── 인용문 패턴 ───────────────────────────────────────
_QUOTE_RE = re.compile(r"^>\s*(.+)$")

# ── 차트 데이터 키 매핑 ──────────────────────────────
_CHART_KEYWORDS = {
    "ESL 시장": "ESL",
    "ESL": "ESL",
    "RMN 광고비": "RMN_AD_SPEND",
    "RMN": "RMN_AD_SPEND",
    "AI in Retail": "AI_IN_RETAIL",
    "AI_IN_RETAIL": "AI_IN_RETAIL",
    "Walmart": "WALMART_CONNECT",
    "월마트": "WALMART_CONNECT",
    "J-Curve": "J_CURVE",
    "J-curve": "J_CURVE",
    "로드맵": "J_CURVE",
}

# ── 레이아웃 힌트 → LayoutType 매핑 ──────────────────
_LAYOUT_KEYWORDS = {
    "전면 배경": LayoutType.FULL_BLEED_IMAGE,
    "표지": LayoutType.TITLE_COVER,
    "감사": LayoutType.THANK_YOU,
    "좌측 텍스트": LayoutType.TWO_COLUMN,
    "좌우": LayoutType.TWO_COLUMN,
    "대비 구조": LayoutType.TWO_COLUMN,
    "그래프": LayoutType.CHART_SLIDE,
    "차트": LayoutType.CHART_SLIDE,
    "비교": LayoutType.COMPARISON_TABLE,
    "테이블": LayoutType.COMPARISON_TABLE,
    "3단": LayoutType.THREE_PILLAR,
    "3-pillar": LayoutType.THREE_PILLAR,
    "타임라인": LayoutType.TIMELINE,
    "인포그래픽": LayoutType.INFOGRAPHIC_NUMBERS,
    "ROI": LayoutType.INFOGRAPHIC_NUMBERS,
    "지도": LayoutType.FULL_BLEED_IMAGE,
    "디바이스": LayoutType.FULL_BLEED_IMAGE,
    "라인업": LayoutType.FULL_BLEED_IMAGE,
    "QR": LayoutType.THANK_YOU,
}


def _infer_layout_type(hint: str, title: str) -> LayoutType:
    """레이아웃 힌트와 제목으로 LayoutType 추론."""
    combined = f"{hint} {title}".lower()
    for keyword, lt in _LAYOUT_KEYWORDS.items():
        if keyword.lower() in combined:
            return lt
    return LayoutType.GENERIC


def _infer_layout_type_b(header: str, title: str, body: str) -> LayoutType:
    """Version B용 LayoutType 추론 (레이아웃 키 없음)."""
    combined = f"{header} {title} {body[:200]}".lower()

    if "표지" in title or "slide 1" in combined:
        return LayoutType.TITLE_COVER
    if "감사" in title or "thank" in combined:
        return LayoutType.THANK_YOU
    if "부록" in title:
        return LayoutType.TEXT_HEAVY_BULLETS

    # 차트 관련
    if "시장 규모" in combined or "market" in combined:
        return LayoutType.CHART_DETAILED
    if "j-curve" in combined or "로드맵" in combined:
        return LayoutType.CHART_DETAILED
    if "월마트" in title and "광고" in combined:
        return LayoutType.CHART_DETAILED

    # 테이블 관련
    if "도입률" in combined or "roi" in combined or "hw 라인업" in combined.lower():
        return LayoutType.TEXT_HEAVY_TABLE
    if "전용 ai" in combined and "범용" in combined:
        return LayoutType.COMPARISON_TABLE

    # 뉴스 인용
    if "뉴스" in combined or "사례" in title:
        return LayoutType.NEWS_QUOTE

    return LayoutType.TEXT_HEAVY_BULLETS


def _infer_layout_type_ir(hint: str, title: str) -> LayoutType:
    """Version IR용 LayoutType 추론 (레이아웃 힌트 기반).

    IR 마크다운은 **레이아웃**: 키를 사용하므로 hint 우선 매칭.
    "3단 분산 AI" 같은 제목과 "3-pillar" 레이아웃을 구분하기 위해
    일부 키워드는 hint에서만 검색한다.
    """
    hint_lower = hint.lower()
    combined = f"{hint} {title}".lower()

    # 1. 표지 / 감사
    if "표지" in combined or "investment proposal" in combined:
        return LayoutType.TITLE_COVER
    if "감사" in combined or "중앙 정렬" in combined:
        return LayoutType.THANK_YOU

    # 2. 텍스트 중심 (불릿)
    if "텍스트 중심" in combined:
        return LayoutType.TEXT_HEAVY_BULLETS

    # 3. 텍스트+테이블 / 테이블 중심 → TEXT_HEAVY_TABLE
    if "텍스트+테이블" in combined or "테이블 중심" in combined:
        return LayoutType.TEXT_HEAVY_TABLE

    # 4. 비교/대비 테이블 → COMPARISON_TABLE
    if "비교" in combined or "대비" in combined:
        return LayoutType.COMPARISON_TABLE

    # 5. 차트 / 그래프 / J-Curve
    if "그래프" in combined or "차트" in combined or "j-curve" in combined:
        return LayoutType.CHART_SLIDE

    # 6. 3-pillar (hint만 검사 — 제목의 "3단 분산"과 혼동 방지)
    if "3-pillar" in hint_lower or "3단" in hint_lower:
        return LayoutType.THREE_PILLAR

    # 7. 타임라인
    if "타임라인" in combined:
        return LayoutType.TIMELINE

    # 8. 좌측/좌우 → TWO_COLUMN (인포그래픽보다 우선 — "좌측+우측 인포그래픽" 대응)
    if "좌측" in combined or "좌우" in combined:
        return LayoutType.TWO_COLUMN

    # 9. 인포그래픽
    if "인포그래픽" in combined:
        return LayoutType.INFOGRAPHIC_NUMBERS

    # 10. 전면 배경
    if "전면 배경" in combined:
        return LayoutType.FULL_BLEED_IMAGE

    return LayoutType.GENERIC


def _detect_chart_keys(text: str) -> list:
    """텍스트에서 차트 데이터 키 감지."""
    keys = []
    for keyword, key in _CHART_KEYWORDS.items():
        if keyword in text and key not in keys:
            keys.append(key)
    return keys


def _parse_table(lines: list) -> dict:
    """마크다운 테이블 행 리스트를 파싱.

    Returns:
        {"headers": [...], "rows": [[...], ...]}
    """
    headers = []
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if _TABLE_SEP_RE.match(line):
            continue
        if not headers:
            headers = cells
        else:
            rows.append(cells)
    return {"headers": headers, "rows": rows}


def _extract_section_info_b(raw: str) -> tuple:
    """Version B의 **헤더**: 라인에서 섹션 정보 추출.

    예: **헤더**: AIsirius | Marketing Opportunity
    → ("시장 기회", "Marketing Opportunity")
    """
    m = re.search(r"\*\*헤더\*\*\s*[:：]\s*(?:AIsirius\s*\|\s*)?(.+)", raw)
    if m:
        english = m.group(1).strip()
        return ("", english)
    return ("", "")


def parse_slides(filepath: str, version: str = "A") -> list:
    """마크다운 파일을 파싱하여 SlideContent 리스트 반환.

    Args:
        filepath: 마크다운 파일 경로
        version: "A", "B", 또는 "IR"

    Returns:
        list[SlideContent]
    """
    text = Path(filepath).read_text(encoding="utf-8")

    # 슬라이드별로 분할
    matches = list(_SLIDE_RE.finditer(text))
    if not matches:
        return []

    slides = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        raw = text[start:end].strip()

        number = int(match.group(1))
        title = match.group(2).strip()

        sc = SlideContent(number=number, title=title, raw_text=raw)

        # 메타 키-값 추출
        for meta_match in _META_RE.finditer(raw):
            key = meta_match.group(1).strip()
            val = meta_match.group(2).strip()

            key_lower = key.lower()
            if "레이아웃" in key:
                sc.layout_hint = val
            elif "헤드라인" in key or "메인 카피" in key:
                sc.headline = val
            elif "노트" in key:
                sc.notes = val
            elif "헤더" in key:
                sc.section_english = val.replace("AIsirius |", "").replace("AIsirius|", "").strip()
            elif "배경" in key:
                sc.image_refs.append(val)

        # 테이블 파싱
        table_lines = []
        in_table = False
        for line in raw.split("\n"):
            if _TABLE_ROW_RE.match(line.strip()):
                in_table = True
                table_lines.append(line.strip())
            elif in_table:
                if table_lines:
                    sc.tables.append(_parse_table(table_lines))
                    table_lines = []
                in_table = False
        if table_lines:
            sc.tables.append(_parse_table(table_lines))

        # 인용문 추출
        for line in raw.split("\n"):
            qm = _QUOTE_RE.match(line.strip())
            if qm:
                sc.quotes.append(qm.group(1).strip())

        # 불릿 추출
        for line in raw.split("\n"):
            bm = _BULLET_RE.match(line.strip())
            if bm:
                sc.bullets.append(bm.group(1).strip())
            else:
                nm = _NUM_BULLET_RE.match(line.strip())
                if nm:
                    sc.bullets.append(nm.group(1).strip())

        # 본문 텍스트 (메타/테이블/불릿/인용문 제외한 일반 텍스트)
        body_lines = []
        in_code = False
        for line in raw.split("\n"):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if stripped.startswith("---"):
                continue
            if _META_RE.match(stripped):
                continue
            if _TABLE_ROW_RE.match(stripped) or _TABLE_SEP_RE.match(stripped):
                continue
            if stripped.startswith(">"):
                continue
            if _BULLET_RE.match(stripped) or _NUM_BULLET_RE.match(stripped):
                continue
            if stripped and not stripped.startswith("#"):
                body_lines.append(stripped)

        sc.body_texts = body_lines

        # 차트 키 감지
        sc.chart_keys = _detect_chart_keys(raw)

        # 레이아웃 타입 추론
        if version == "A":
            sc.layout_type = _infer_layout_type(sc.layout_hint, title)
        elif version == "IR":
            sc.layout_type = _infer_layout_type_ir(sc.layout_hint, title)
        else:
            sc.layout_type = _infer_layout_type_b(
                sc.section_english, title, raw
            )

        # 표지/감사 슬라이드 강제 매핑
        if number == 1:
            sc.layout_type = LayoutType.TITLE_COVER

        slides.append(sc)

    return slides
