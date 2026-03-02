# IRdeck

AIsirius(에이아이시리우스) 투자제안서 / 회사소개서 / 파트너제안서 자동 생성 프로젝트

## Overview

기존 PPT/DOCX 문서(~70개)를 분석하여 핵심 소구 포인트를 추출하고, 대상별 맞춤 프레젠테이션을 자동 생성합니다.

### 생성 버전
| 버전 | 특징 | 슬라이드 |
|------|------|----------|
| **Ver.A** (비주얼) | 이미지/인포그래픽 중심, 투자자/파트너용 | 25장 |
| **Ver.B** (텍스트 상세) | 데이터/표 중심, 실무 검토용 | 28장 |

## 프로젝트 구조

```
IRdeck/
├── docs/
│   ├── analysis/          # 기존 문서 분석 결과 (5계열, 20개 소구포인트)
│   ├── content/           # 슬라이드별 콘텐츠 원고 (Ver.A/B)
│   └── references/        # 시장 데이터, 참고 자료
├── scripts/
│   ├── build_deck.py      # PPTX 자동 빌드 (메인)
│   ├── generate_gamma.py  # Gamma.app API 연동
│   ├── watermark_pdf.py   # 워터마크 PDF 생성
│   └── components/        # 브랜드 디자인 컴포넌트
│       ├── colors.py      # 14색 브랜드 컬러
│       ├── fonts.py       # 폰트 설정 (에스코어 드림, 맑은 고딕)
│       ├── layouts.py     # 레이아웃 좌표/타입 (18종)
│       ├── chrome.py      # 헤더/푸터/로고 크롬 요소
│       ├── charts.py      # 차트/테이블 (ESL, RMN, AI 시장)
│       └── markdown_parser.py  # Markdown → SlideContent 파서
├── templates/             # PPTX 템플릿
├── assets/                # 이미지, 인포그래픽, 차트, 아이콘
├── designs/               # Pencil 디자인 파일 (.pen)
└── output/                # 생성된 최종 PPTX/PDF
```

## 사용법

### PPTX 빌드

```bash
# Ver.A (비주얼) 빌드
python scripts/build_deck.py --version A

# Ver.B (텍스트 상세) 빌드
python scripts/build_deck.py --version B

# 전체 빌드 + 워터마크 PDF
python scripts/build_deck.py --version all --watermark
```

### Gamma.app 연동

```bash
python scripts/generate_gamma.py --version A --api-key "sk-gamma-xxx" --export pptx
```

### 워터마크 PDF

```bash
python scripts/watermark_pdf.py input.pptx --company "대상사명" --output output.pdf
```

## 기술 스택

- **문서 생성**: python-pptx, python-docx
- **이미지/인포그래픽**: 나노바나나2 (ComfyUI 기반)
- **디자인 프로토타입**: Pencil (.pen)
- **AI 프레젠테이션**: Gamma.app API
- **AI 콘텐츠**: Claude Code

## 브랜드 디자인

| 요소 | 값 |
|------|-----|
| Primary | Dark Navy `#0E1D62` |
| Accent | Brand Cyan `#32EDF6` |
| Secondary | Standard Blue `#0070C0` |
| 한글 폰트 | 에스코어 드림, 맑은 고딕 |
| 영문 폰트 | Arial |
| 슬라이드 | 16:9 (1920x1080) |

## License

Private - AIsirius Co., Ltd.
