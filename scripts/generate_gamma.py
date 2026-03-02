"""Gamma.app API를 통한 프레젠테이션 자동 생성.

AIsirius 콘텐츠를 Gamma API로 전송하여 디자인된 PPT를 생성한다.

API 문서: https://developers.gamma.app/docs/getting-started
Base URL: https://public-api.gamma.app/v1.0/

Usage:
    python scripts/generate_gamma.py --version A
    python scripts/generate_gamma.py --version B
    python scripts/generate_gamma.py --version A --export pptx
    python scripts/generate_gamma.py --api-key "sk-gamma-xxxxx"

사전 조건:
    - Gamma Pro 계정 이상 (API 키 필요)
    - API 키: Gamma Settings > API key 탭에서 생성
"""
import argparse
import io
import json
import os
import sys
import time
from pathlib import Path

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

try:
    import requests
except ImportError:
    print("[ERROR] requests 패키지가 필요합니다: pip install requests")
    sys.exit(1)

# 프로젝트 경로
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
CONTENT_DIR = os.path.join(PROJECT_ROOT, "docs", "content")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output", "회사소개서")
CREDENTIALS_FILE = os.path.join(PROJECT_ROOT, "docs", "credentials.md")

# Gamma API
GAMMA_API_BASE = "https://public-api.gamma.app/v1.0"


def load_api_key(cli_key=None):
    """API 키 로드 (CLI 인자 > 환경변수 > credentials.md)."""
    if cli_key:
        return cli_key

    env_key = os.environ.get("GAMMA_API_KEY")
    if env_key:
        return env_key

    # credentials.md에서 키 찾기
    if os.path.exists(CREDENTIALS_FILE):
        text = Path(CREDENTIALS_FILE).read_text(encoding="utf-8")
        for line in text.split("\n"):
            if "gamma" in line.lower() and "sk-gamma-" in line:
                # sk-gamma-xxxxxxxx 패턴 추출
                import re
                m = re.search(r"(sk-gamma-\S+)", line)
                if m:
                    return m.group(1)

    return None


def load_content(version):
    """마크다운 콘텐츠 파일을 Gamma inputText용으로 로드."""
    if version == "A":
        filepath = os.path.join(CONTENT_DIR, "슬라이드_세부내용_VerA_비주얼.md")
    else:
        filepath = os.path.join(CONTENT_DIR, "슬라이드_세부내용_VerB_텍스트상세.md")

    text = Path(filepath).read_text(encoding="utf-8")

    # Gamma에 전송할 콘텐츠 구성
    intro = """# AIsirius 회사소개서

에이아이시리우스(AIsirius)는 리테일 전문 AI 기업입니다.
AI 기술로 오프라인 매장을 지능형 미디어 공간으로 전환합니다.

브랜드 컬러: Dark Navy (#0E1D62), Cyan (#32EDF6), Blue (#0070C0)
슬로건: "Store into Media, Shelf into Profit"

"""
    return intro + text


def generate_presentation(api_key, content, version, num_cards=25, export_format=None):
    """Gamma Generate API 호출.

    Args:
        api_key: Gamma API 키
        content: 프레젠테이션 콘텐츠 텍스트
        version: "A" or "B"
        num_cards: 슬라이드 수
        export_format: "pptx" or "pdf" or None

    Returns:
        dict: API 응답
    """
    url = f"{GAMMA_API_BASE}/generate"

    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json",
    }

    # Version에 따른 파라미터 조정
    if version == "A":
        text_amount = "brief"
        text_mode = "condense"
        additional = (
            "This is a visual-heavy company introduction presentation for AIsirius, "
            "a retail-specialized AI company. Use minimal text with large visuals. "
            "Brand colors: Dark Navy #0E1D62, Cyan #32EDF6, Blue #0070C0. "
            "Style: Modern, clean, tech-forward."
        )
    else:
        text_amount = "detailed"
        text_mode = "preserve"
        additional = (
            "This is a text-heavy company introduction for AIsirius, "
            "a retail-specialized AI company. Preserve all detailed text and data. "
            "CEO prefers dense text with bold emphasis. "
            "Brand colors: Dark Navy #0E1D62, Cyan #32EDF6, Blue #0070C0. "
            "Include all market data tables and news citations."
        )

    payload = {
        "inputText": content,
        "textMode": text_mode,
        "format": "presentation",
        "numCards": num_cards,
        "additionalInstructions": additional,
        "textOptions": {
            "amount": text_amount,
            "language": "ko",
            "audience": "투자자 및 파트너사",
        },
        "imageOptions": {
            "source": "aiGenerated",
            "style": "modern corporate tech, clean minimal, dark navy and cyan accent",
        },
        "cardOptions": {
            "dimensions": "16x9",
        },
    }

    # 내보내기 옵션
    if export_format:
        payload["exportAs"] = export_format

    print(f"[INFO] Gamma API 호출 중... (Version {version}, {num_cards}장)")
    print(f"  콘텐츠 길이: {len(content):,}자")

    response = requests.post(url, headers=headers, json=payload, timeout=120)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 202:
        # 비동기 처리 — 결과 폴링
        result = response.json()
        job_id = result.get("id") or result.get("jobId")
        print(f"  비동기 작업 시작: {job_id}")
        return poll_result(api_key, job_id)
    else:
        print(f"[ERROR] API 응답 {response.status_code}: {response.text[:500]}")
        return None


def poll_result(api_key, job_id, max_wait=300):
    """비동기 작업 결과 폴링."""
    headers = {"X-API-KEY": api_key}
    url = f"{GAMMA_API_BASE}/generate/{job_id}"

    start = time.time()
    while time.time() - start < max_wait:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            result = response.json()
            status = result.get("status", "")
            if status in ("completed", "done", "success"):
                return result
            if status in ("failed", "error"):
                print(f"[ERROR] 작업 실패: {result}")
                return None
            print(f"  상태: {status}... ({int(time.time()-start)}초 경과)")
        time.sleep(5)

    print(f"[ERROR] 타임아웃 ({max_wait}초)")
    return None


def download_export(api_key, gamma_id, export_format, output_path):
    """생성된 Gamma를 PPT/PDF로 내보내기."""
    headers = {"X-API-KEY": api_key}
    url = f"{GAMMA_API_BASE}/gammas/{gamma_id}/export"

    params = {"format": export_format}
    response = requests.get(url, headers=headers, params=params, timeout=120)

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"[OK] 내보내기 완료: {output_path}")
        return output_path
    else:
        print(f"[ERROR] 내보내기 실패 {response.status_code}: {response.text[:300]}")
        return None


def main():
    parser = argparse.ArgumentParser(description="Gamma.app PPT Generator")
    parser.add_argument("--version", choices=["A", "B", "all"], default="all",
                        help="생성 버전 (A=비주얼, B=텍스트상세)")
    parser.add_argument("--api-key", default=None,
                        help="Gamma API 키 (sk-gamma-xxxxx)")
    parser.add_argument("--export", choices=["pptx", "pdf"], default="pptx",
                        help="내보내기 형식")
    parser.add_argument("--cards", type=int, default=25,
                        help="슬라이드 수 (기본: 25)")
    args = parser.parse_args()

    print("=" * 60)
    print("  Gamma.app PPT Generator")
    print("=" * 60)

    # API 키 로드
    api_key = load_api_key(args.api_key)
    if not api_key:
        print("\n[ERROR] Gamma API 키가 필요합니다.")
        print("  방법 1: --api-key 'sk-gamma-xxxxx' 인자")
        print("  방법 2: GAMMA_API_KEY 환경변수 설정")
        print("  방법 3: docs/credentials.md에 기록")
        print("\n  API 키 발급: gamma.app > Settings > API key")
        sys.exit(1)

    print(f"  API 키: {api_key[:12]}...")

    versions = ["A", "B"] if args.version == "all" else [args.version]
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for ver in versions:
        print(f"\n{'─' * 50}")
        print(f"  Version {ver} 생성 시작")
        print(f"{'─' * 50}")

        content = load_content(ver)
        result = generate_presentation(
            api_key, content, ver,
            num_cards=args.cards,
            export_format=args.export,
        )

        if result:
            gamma_id = result.get("id") or result.get("gammaId")
            gamma_url = result.get("url") or result.get("gammaUrl")

            print(f"\n  Gamma ID: {gamma_id}")
            if gamma_url:
                print(f"  Gamma URL: {gamma_url}")

            # 결과 저장
            result_path = os.path.join(
                OUTPUT_DIR, f"gamma_result_Ver{ver}.json"
            )
            with open(result_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"  API 응답 저장: {result_path}")

            # PPT 내보내기 (exportAs가 응답에 포함된 경우)
            export_url = result.get("exportUrl")
            if export_url:
                output_path = os.path.join(
                    OUTPUT_DIR,
                    f"AIsirius_회사소개서_Gamma_Ver{ver}.{args.export}"
                )
                print(f"  내보내기 다운로드 중...")
                import urllib.request
                urllib.request.urlretrieve(export_url, output_path)
                print(f"[OK] 저장 완료: {output_path}")
            elif gamma_id:
                # 별도 내보내기 API 호출
                output_path = os.path.join(
                    OUTPUT_DIR,
                    f"AIsirius_회사소개서_Gamma_Ver{ver}.{args.export}"
                )
                download_export(api_key, gamma_id, args.export, output_path)
        else:
            print(f"[ERROR] Version {ver} 생성 실패")

    print(f"\n{'=' * 60}")
    print("  완료!")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
