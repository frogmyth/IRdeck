"""AIsirius PPTX 템플릿 생성 스크립트.

16:9 빈 프레젠테이션에 슬라이드 마스터 배경을 설정하고,
templates/ 디렉토리에 Version A/B 템플릿을 저장한다.

Usage:
    python scripts/create_templates.py
"""
import os
import sys

# 프로젝트 루트를 path에 추가
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.oxml.ns import qn

from components.colors import WHITE, LIGHT_GRAY
from components.layouts import SLIDE_WIDTH, SLIDE_HEIGHT


# 프로젝트 경로
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "templates")


def create_base_presentation():
    """16:9 빈 프레젠테이션 생성."""
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    return prs


def create_template_a():
    """Version A (비주얼형) 템플릿 생성.

    - 흰색 배경
    - Blank 레이아웃 사용 (크롬은 build_deck에서 per-slide 추가)
    """
    prs = create_base_presentation()
    output_path = os.path.join(TEMPLATES_DIR, "aisirius_template_A.pptx")
    prs.save(output_path)
    print(f"[OK] Version A template: {output_path}")
    return output_path


def create_template_b():
    """Version B (텍스트 상세형) 템플릿 생성.

    - 흰색 배경
    - Blank 레이아웃 사용 (크롬은 build_deck에서 per-slide 추가)
    """
    prs = create_base_presentation()
    output_path = os.path.join(TEMPLATES_DIR, "aisirius_template_B.pptx")
    prs.save(output_path)
    print(f"[OK] Version B template: {output_path}")
    return output_path


def main():
    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    print("=== AIsirius PPTX 템플릿 생성 ===")
    create_template_a()
    create_template_b()
    print("\n완료. templates/ 디렉토리를 확인하세요.")


if __name__ == "__main__":
    main()
