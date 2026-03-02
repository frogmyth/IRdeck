# AIsirius 회사소개서 — 이미지 프롬프트 & 소싱 가이드

> 작성일: 2026-03-02
> 대상: 회사소개서 25장 슬라이드용 전체 이미지 가이드
> 소스 이미지 경로: `G:\00.googledrive\07.AIsirius\20.회사소개서\images\` (470 files)
> Nanobanana2 서버: `121.165.20.68:8188` (ComfyUI / SDXL 기반)
> 브랜드 컬러: Dark Navy `#0E1D62` | Cyan `#32EDF6` | Blue `#0070C0` | Bright Blue `#00B0F0`

---

## 목차

1. [이미지 분류 총괄표](#1-이미지-분류-총괄표)
2. [기존 이미지에서 소싱 (Section A)](#2-기존-이미지에서-소싱-section-a)
3. [웹 다운로드 필요 (Section B)](#3-웹-다운로드-필요-section-b)
4. [Nanobanana2 AI 생성 프롬프트 (Section C)](#4-nanobanana2-ai-생성-프롬프트-section-c)
5. [Midjourney 대체 프롬프트 (Section D)](#5-midjourney-대체-프롬프트-section-d)
6. [python-pptx 차트 (참고)](#6-python-pptx-차트-참고)
7. [QR 코드 생성](#7-qr-코드-생성)

---

## 1. 이미지 분류 총괄표

| 슬라이드 | 제목 | 필요 이미지 | 소싱 방식 | 저장 위치 |
|----------|------|-----------|----------|----------|
| 1 | 표지 | 로고 + 미래형 매장 배경 | 기존(로고) + AI생성(배경) | `images/` + `infographics/` |
| 2 | 한 줄 정의 | 포지셔닝 계층도 배경 | AI생성 | `infographics/` |
| 3 | DX→AX | 패러다임 전환 배경 | AI생성 | `infographics/` |
| 4 | 글로벌 시장 규모 | 차트 배경 | AI생성 (배경만) | `charts/` |
| 5 | 월마트 사례 | 월마트 매장/로고 | 웹다운로드 | `images/` |
| 6 | ESL 교체 시점 | 세계 지도 배경 | AI생성 | `infographics/` |
| 7 | AI 3-pillar | 3-pillar 인포그래픽 배경 | AI생성 | `infographics/` |
| 8 | 전용 AI vs 범용 AI | 비교 배경 + AI 생성물 예시 | 기존(AI생성물) + AI생성(배경) | `images/` + `infographics/` |
| 9 | AI 콘텐츠 데모 | CMS 스크린샷 + AI 생성물 | 기존 | `images/` |
| 10 | AI 매장 분석 | 데이터 흐름도 배경 | AI생성 | `infographics/` |
| 11 | 3단 분산 AI | 아키텍처 다이어그램 배경 | AI생성 | `infographics/` |
| 12 | 리테일 미디어 플랫폼 | 플랫폼 아키텍처 배경 | AI생성 | `infographics/` |
| 13 | CMS 주요 기능 | CMS 스크린샷 6개 | 기존 | `images/` |
| 14 | 크로스 디바이스 | 시연 사진/캡처 | 기존 | `images/` |
| 15 | HW 라인업 | 디바이스 사진 (23", 29", 사이니지, EPD) | 기존 | `images/` |
| 16 | 기존 기기 흡수 | before/after 배경 | AI생성 | `infographics/` |
| 17 | 하이브리드 수익 모델 | 피라미드 인포그래픽 배경 | AI생성 | `infographics/` |
| 18 | ROI 분석 | ROI 인포그래픽 배경 | AI생성 | `infographics/` |
| 19 | 글로벌 전략 | 세계 지도 + 파트너 로고 | AI생성(지도) + 웹다운로드(로고) | `infographics/` + `images/` |
| 20 | J-Curve 로드맵 | 차트 배경 | AI생성 (배경만) | `charts/` |
| 21 | CEO & 팀 | CEO 사진 + 팀 구성도 배경 | 기존(CEO) + AI생성(배경) | `images/` + `infographics/` |
| 22 | 국내 트랙션 | 타임라인 배경 + 성과 사진 | 기존(사진) + AI생성(배경) | `images/` + `infographics/` |
| 23 | ESG | ESG 아이콘 3개 | AI생성 | `icons/` |
| 24 | 감사합니다 | 로고 + QR코드 | 기존(로고) + 생성(QR) | `images/` |
| 25 | 부록 | 대상별 상이 | 기존 + AI생성 | 다양 |

---

## 2. 기존 이미지에서 소싱 (Section A)

> 소스: `G:\00.googledrive\07.AIsirius\20.회사소개서\images\` (470 files)
> 아래 경로는 소스 디렉토리 내 예상 하위 분류 기준. 실제 파일명 확인 후 복사.

### A-01. 로고 (Slides 1, 24)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-01-1 | AIsirius 로고 (흰색 버전) | `images/logos/` | `assets/images/logo_white.png` | 표지 + 마지막 장 |
| A-01-2 | AIsirius 로고 (컬러 버전) | `images/logos/` | `assets/images/logo_color.png` | 내부 슬라이드용 |
| A-01-3 | AIsirius 로고 (다크 배경용) | `images/logos/` | `assets/images/logo_dark_bg.png` | 다크 네이비 배경 |
| A-01-4 | ISO4OM 브랜드 마크 | `images/logos/` | `assets/images/iso4om_mark.png` | 있으면 사용 |

### A-02. 제품/디바이스 사진 (Slides 14, 15)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-02-1 | Stretched LCD 23인치 (60x6cm) | `images/products/` | `assets/images/lcd_23inch.png` | HW 라인업 슬라이드 |
| A-02-2 | Stretched LCD 29인치 (70x23cm) | `images/products/` | `assets/images/lcd_29inch.png` | HW 라인업 슬라이드 |
| A-02-3 | 일반 사이니지 (10~75인치) | `images/products/` | `assets/images/signage_general.png` | HW 라인업 |
| A-02-4 | EPD (전자잉크 디스플레이) | `images/products/` | `assets/images/epd_device.png` | HW 라인업 |
| A-02-5 | 디바이스 매장 설치 사진 | `images/products/` | `assets/images/device_installed.png` | 크로스 디바이스 슬라이드 |
| A-02-6 | 터치 인터랙션 시연 사진 | `images/products/` | `assets/images/touch_demo.png` | 크로스 디바이스 |
| A-02-7 | 게이미피케이션 (버블 터뜨리기) 캡처 | `images/products/` | `assets/images/gamification.png` | 크로스 디바이스 |

### A-03. CMS 스크린샷 (Slides 9, 13)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-03-1 | CMS 메인 대시보드 | `images/cms_screenshots/` | `assets/images/cms_dashboard.png` | CMS 주요 기능 |
| A-03-2 | CMS 태그 관리 화면 | `images/cms_screenshots/` | `assets/images/cms_tag_mgmt.png` | 실시간 태그 관리 |
| A-03-3 | CMS 플래노그램 편집기 | `images/cms_screenshots/` | `assets/images/cms_planogram.png` | 플래노그램 편집 |
| A-03-4 | CMS 예약 스케줄링 화면 | `images/cms_screenshots/` | `assets/images/cms_scheduling.png` | 예약 스케줄링 |
| A-03-5 | CMS 프로모션 설정 화면 | `images/cms_screenshots/` | `assets/images/cms_promotion.png` | 프로모션 자동화 |
| A-03-6 | PDA 앱 화면 (바코드 스캔) | `images/cms_screenshots/` | `assets/images/pda_app.png` | PDA 현장 관리 |
| A-03-7 | AI 이미지 생성 화면 (CMS 내) | `images/cms_screenshots/` | `assets/images/cms_ai_gen.png` | AI 콘텐츠 데모 |

### A-04. AI 생성물 예시 (Slides 8, 9)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-04-1 | AI 생성 이벤트 배너 (HAPPY NEW YEAR) | `images/ai_generated/` | `assets/images/ai_sample_banner.png` | AI 콘텐츠 데모 |
| A-04-2 | AI 생성 3D 피규어/캐릭터 | `images/ai_generated/` | `assets/images/ai_sample_figure.png` | AI 콘텐츠 데모 |
| A-04-3 | AI 생성 바게트 이미지 → 동영상 예시 | `images/ai_generated/` | `assets/images/ai_sample_baguette.png` | AI 콘텐츠 데모 |
| A-04-4 | 범용 AI 왜곡 예시 (비교용) | `images/ai_generated/` | `assets/images/generic_ai_bad.png` | 전용 vs 범용 비교 |
| A-04-5 | AIsirius 전용 AI 정확 예시 (비교용) | `images/ai_generated/` | `assets/images/aisirius_ai_good.png` | 전용 vs 범용 비교 |
| A-04-6 | 비정형 해상도 생성물 (1920x158 등) | `images/ai_generated/` | `assets/images/ai_stretched.png` | 전용 AI 차별점 |

### A-05. CEO/팀 사진 (Slide 21)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-05-1 | 김현학 CEO 프로필 사진 | `images/` 또는 별도 폴더 | `assets/images/ceo_photo.png` | CEO & 팀 슬라이드 |

### A-06. 트랙션/성과 사진 (Slide 22)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-06-1 | 인탑스/DK 시연 현장 사진 | `images/` | `assets/images/demo_intops.png` | 국내 트랙션 |
| A-06-2 | 회의실 안내 시스템 설치 사진 | `images/` | `assets/images/meeting_room.png` | 경기R&DB 센터 |
| A-06-3 | TGCS 파트너십 체결 사진 (있으면) | `images/` | `assets/images/tgcs_signing.png` | 트랙션 |
| A-06-4 | TCS MOU 체결 사진 (있으면) | `images/` | `assets/images/tcs_mou.png` | 트랙션 |

### A-07. 배경/스톡 이미지 (다양한 슬라이드)

| ID | 용도 | 예상 소스 경로 | 복사 대상 | 비고 |
|----|------|-------------|----------|------|
| A-07-1 | 매장 내부 사진 (기존 스톡) | `images/stock/` | `assets/images/store_interior.png` | 표지 후보 (AI생성 대신 사용 가능) |
| A-07-2 | 리테일 기술 배경 | `images/backgrounds/` | `assets/images/retail_tech_bg.png` | 다양한 슬라이드 배경 |

---

## 3. 웹 다운로드 필요 (Section B)

> 파트너사 로고 및 참조 이미지. 투명 배경(PNG) 권장.
> 상업적 사용이므로 공식 미디어 킷/브랜드 가이드에서 다운로드.

### B-01. 파트너사 로고 (Slide 19)

| ID | 이미지 | 다운로드 소스 | 저장 경로 | 크기 | 비고 |
|----|--------|-------------|----------|------|------|
| B-01-1 | **TGCS (Toshiba Global Commerce Solutions) 로고** | [TGCS 공식](https://commerce.toshiba.com/) Media Kit | `assets/images/logo_tgcs.png` | 400x200px | 흰색 배경 + 투명 배경 두 버전 |
| B-01-2 | **TCS (Tata Consultancy Services) 로고** | [TCS 미디어 센터](https://www.tcs.com/media) | `assets/images/logo_tcs.png` | 400x200px | 공식 브랜드 가이드 준수 |
| B-01-3 | **NRI (Nomura Research Institute) 로고** | [NRI 공식](https://www.nri.com/) | `assets/images/logo_nri.png` | 400x200px | 일본 SI 파트너 |
| B-01-4 | **Toshiba Tec 로고** | [Toshiba Tec](https://www.toshibatec.co.jp/) | `assets/images/logo_toshiba_tec.png` | 400x200px | 일본 시장 |
| B-01-5 | **SCSK 로고** | [SCSK 공식](https://www.scsk.jp/) | `assets/images/logo_scsk.png` | 400x200px | 일본 SI |

### B-02. 참조 이미지 (Slide 5)

| ID | 이미지 | 다운로드 소스 | 저장 경로 | 비고 |
|----|--------|-------------|----------|------|
| B-02-1 | **Walmart 로고** | [Walmart 브랜드 센터](https://corporate.walmart.com/newsroom/brand-center) | `assets/images/logo_walmart.png` | 월마트 사례 슬라이드 |
| B-02-2 | **Walmart Connect 로고** | 검색: "Walmart Connect logo" | `assets/images/logo_walmart_connect.png` | 광고 매출 그래프 옆 |
| B-02-3 | **Walmart 매장 내부 ESL 사진** (있으면) | 뉴스 기사/Press Release | `assets/images/walmart_store_esl.png` | 참고 사진 (저작권 확인 필요) |

### B-03. 중국 HW 파트너 로고 (Slide 15, 19)

| ID | 이미지 | 다운로드 소스 | 저장 경로 | 비고 |
|----|--------|-------------|----------|------|
| B-03-1 | **Yes Optoelectronics 로고** | 파트너사에 직접 요청 | `assets/images/logo_yes_opto.png` | HW 소싱 파트너 |
| B-03-2 | **HonorLink 로고** | 파트너사에 직접 요청 | `assets/images/logo_honorlink.png` | HW 소싱 파트너 |

---

## 4. Nanobanana2 AI 생성 프롬프트 (Section C)

> 서버: `121.165.20.68:8188` (ComfyUI)
> 모델: SDXL 기반 (Z-image / Flux.2 사용 가능)
> 프롬프트 형식: ComfyUI/SDXL 스타일 (positive + negative prompt)
> 인포그래픽 규칙: 텍스트는 이미지에 포함하지 않음 (python-pptx 오버레이)

### C-01. 표지 배경 — 미래형 매장 내부 (Slide 1)

```
파일명: assets/infographics/slide01_cover_bg.png
슬라이드: #1 (표지)
용도: 전면 배경 이미지 (텍스트 오버레이 예정)
크기: 3840 x 2160 px (16:9 4K, 축소 사용)
스타일: 미래적, 깔끔, 네이비+시안 톤
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
futuristic retail store interior, modern supermarket aisle with digital LED shelf displays,
stretched LCD screens on shelf edges showing product information, blue and cyan ambient lighting,
clean minimalist design, glass shelves, dark navy (#0E1D62) and cyan (#32EDF6) color accent,
high-tech smart store atmosphere, volumetric lighting, photorealistic, 8k, ultra detailed,
professional commercial photography, wide angle lens, depth of field blur on background,
no text, no logos, no watermarks
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, blurry, low quality, cartoon, anime, illustration,
people, customers, crowded, messy shelves, traditional store, paper labels, old-fashioned,
warm yellow lighting, red tones, neon signs, oversaturated
```

**ComfyUI 설정:**
- Checkpoint: SDXL / Z-image
- Steps: 30-40
- CFG: 7.0
- Sampler: DPM++ 2M Karras
- Size: 1920x1080 (upscale to 3840x2160)

---

### C-02. 포지셔닝 계층도 배경 (Slide 2)

```
파일명: assets/infographics/slide02_positioning_bg.png
슬라이드: #2 (한 줄 정의)
용도: 우측 인포그래픽 영역 배경 (도형+텍스트는 python-pptx 오버레이)
크기: 1920 x 1080 px
스타일: 추상적 계층 구조 느낌, 네이비 그라디언트
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract technology background, dark navy blue gradient (#0E1D62 to #0070C0),
subtle geometric shapes, layered horizontal bands with soft glow,
connected dots and lines forming hierarchy pattern, neural network visualization,
futuristic data flow, minimalist corporate design, clean,
soft cyan (#32EDF6) accent lights, bokeh light particles,
dark background with luminous elements, no text, no logos
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, bright background, white background,
colorful, rainbow, cartoon, noisy, cluttered, complex patterns, people, faces
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.5

---

### C-03. DX→AX 패러다임 전환 배경 (Slide 3)

```
파일명: assets/infographics/slide03_dx_ax_bg.png
슬라이드: #3 (DX에서 AX로)
용도: 좌우 대비 배경 (좌=회색/DX, 우=블루/AX)
크기: 1920 x 1080 px
스타일: 좌측 회색톤(과거) → 우측 블루/시안(미래) 그라디언트 전환
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract split background, left side monochrome gray industrial automation,
right side glowing blue and cyan futuristic AI technology,
smooth gradient transition in the center, left: mechanical gears and circuits in grayscale,
right: glowing neural network nodes and AI brain hologram in blue (#0070C0) and cyan (#32EDF6),
dark navy (#0E1D62) base, corporate presentation background,
clean minimalist design, no text, no logos, no watermark
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, people, faces, bright white,
red, green, yellow, cartoon, illustration, messy, noisy, cluttered
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 30
- CFG: 7.0

---

### C-04. 차트 배경 — 시장 규모 (Slide 4)

```
파일명: assets/charts/slide04_market_chart_bg.png
슬라이드: #4 (글로벌 시장 규모)
용도: 차트 영역 배경 (차트 자체는 python-pptx로 생성)
크기: 1920 x 1080 px
스타일: 어두운 네이비, 미세 그리드 라인, 데이터 시각화 느낌
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
dark navy blue background (#0E1D62) with subtle grid lines,
financial data visualization aesthetic, faint dotted grid pattern,
soft blue (#0070C0) glow at bottom edge, minimal abstract chart lines in background,
professional business presentation slide background,
very clean, very subtle, almost solid dark background with minimal texture,
no text, no numbers, no logos, no watermark
```

**Negative Prompt:**
```
text, numbers, words, letters, logos, watermark, charts, graphs, bright,
white background, colorful, busy pattern, people, complex elements
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 20
- CFG: 8.0

---

### C-05. 세계 지도 — ESL 교체 (Slide 6)

```
파일명: assets/infographics/slide06_world_map_esl.png
슬라이드: #6 (ESL 교체 시점 2028)
용도: 지역별 ESL 도입률 표시용 배경 지도 (수치/텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 다크 네이비 배경, 도트/폴리곤 스타일 세계 지도
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract world map made of glowing dots and connected lines on dark navy background (#0E1D62),
digital world map visualization, continents formed by blue (#0070C0) and cyan (#32EDF6) luminous dots,
network connections between major cities, futuristic global data visualization,
subtle glow effect, dark background, clean presentation style,
highlight spots on USA, Europe, Japan, South Korea, China,
no text, no labels, no country names, no logos, no watermark
```

**Negative Prompt:**
```
text, words, letters, labels, country names, numbers, logos, watermark,
traditional map, colorful political map, realistic earth, satellite view,
bright background, cartoon, illustration
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 30
- CFG: 7.0

---

### C-06. AI 3-Pillar 인포그래픽 배경 (Slide 7)

```
파일명: assets/infographics/slide07_3pillar_bg.png
슬라이드: #7 (리테일 전문 AI 3대 핵심)
용도: 3-pillar 인포그래픽 배경 (아이콘+텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 3개 기둥/영역이 구분되는 추상 배경
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract dark background with three vertical glowing pillars of light,
three distinct illuminated columns evenly spaced, left pillar cyan (#32EDF6),
center pillar blue (#0070C0), right pillar bright blue (#00B0F0),
dark navy (#0E1D62) base background, subtle light rays from each pillar,
futuristic technology aesthetic, clean minimalist corporate design,
soft gradient glow, bokeh particles, no text, no logos, no icons, no watermark
```

**Negative Prompt:**
```
text, words, letters, icons, logos, watermark, people, complex scene,
bright background, white, realistic architecture, actual pillars,
columns, classical, ornate, busy, cluttered
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.5

---

### C-07. 전용 AI vs 범용 AI 비교 배경 (Slide 8)

```
파일명: assets/infographics/slide08_ai_comparison_bg.png
슬라이드: #8 (전용 AI vs 범용 AI)
용도: 좌우 대비 테이블 배경
크기: 1920 x 1080 px
스타일: 좌측 흐릿/제한적(범용) vs 우측 선명/강력(전용)
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
split comparison background, left side: blurred unfocused gray-blue area with restriction symbols,
dimmed and desaturated, cloudy digital noise,
right side: sharp clear focused glowing blue (#0070C0) and cyan (#32EDF6) technology,
bright clean precise geometric shapes, confident powerful glow,
dark navy (#0E1D62) background, vertical dividing line in center with soft glow,
corporate presentation style, clean, no text, no logos, no watermark
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, people, faces,
bright white background, cartoon, anime, colorful rainbow,
red, green, yellow, messy, noisy
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.0

---

### C-08. 데이터 흐름도 배경 (Slide 10)

```
파일명: assets/infographics/slide10_data_flow_bg.png
슬라이드: #10 (AI 매장 분석)
용도: 데이터 흐름 다이어그램 배경 (화살표/텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 데이터 파이프라인/플로우 느낌
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract data pipeline visualization background, flowing data streams from left to right,
horizontal glowing lines and arrows in blue (#0070C0) and cyan (#32EDF6),
dark navy (#0E1D62) background, subtle matrix-like data particles,
four connected node points along horizontal axis with soft circular glows,
futuristic data processing aesthetic, network topology,
clean corporate style, no text, no numbers, no labels, no logos, no watermark
```

**Negative Prompt:**
```
text, words, numbers, labels, logos, watermark, bright background,
white, cartoon, people, complex diagram, actual charts,
messy wires, cluttered
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.0

---

### C-09. 3단 분산 AI 아키텍처 배경 (Slide 11)

```
파일명: assets/infographics/slide11_3tier_arch_bg.png
슬라이드: #11 (3단 분산 AI 시스템 — 특허)
용도: 3계층 아키텍처 다이어그램 배경 (텍스트/박스는 오버레이)
크기: 1920 x 1080 px
스타일: 3단 레이어가 시각적으로 구분되는 수평 구조
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract three-layer horizontal architecture visualization,
bottom layer: small scattered glowing edge device dots in cyan (#32EDF6),
middle layer: medium glowing nodes as access points in blue (#0070C0),
top layer: large central server glow in bright blue (#00B0F0),
dark navy (#0E1D62) background, vertical connection lines between layers,
upward data flow arrows as subtle light trails,
hierarchical technology infrastructure aesthetic, clean minimalist design,
no text, no labels, no logos, no watermark
```

**Negative Prompt:**
```
text, words, labels, numbers, logos, watermark, bright background,
white, cartoon, people, faces, complex details, cluttered,
server rack photos, actual hardware
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 30
- CFG: 7.0

---

### C-10. 플랫폼 아키텍처 배경 (Slide 12)

```
파일명: assets/infographics/slide12_platform_arch_bg.png
슬라이드: #12 (리테일 미디어 플랫폼)
용도: 4-Layer 아키텍처 배경 (레이어 텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 4단 수평 레이어 구조, 위로 갈수록 밝아지는 그라디언트
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract four horizontal layered platform visualization,
stacked horizontal bands from bottom to top with increasing brightness,
bottom band: dark solid hardware elements,
second band: subtle device icons glow,
third band: software platform glow in blue (#0070C0),
top band: brightest AI layer glow in cyan (#32EDF6),
dark navy (#0E1D62) base, soft gradient transitions between layers,
corporate technology stack aesthetic, clean and professional,
no text, no labels, no icons, no logos, no watermark
```

**Negative Prompt:**
```
text, words, labels, numbers, logos, watermark, bright background,
white, cartoon, people, cluttered, busy pattern, noisy
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.0

---

### C-11. Before/After 기기 흡수 배경 (Slide 16)

```
파일명: assets/infographics/slide16_before_after_bg.png
슬라이드: #16 (기존 기기 흡수력)
용도: 좌우 Before/After 대비 배경
크기: 1920 x 1080 px
스타일: 좌측 분산/단절 → 우측 통합/연결
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract split comparison background for before and after concept,
left side: scattered disconnected floating rectangles in gray tones,
fragmented isolated devices, dull disconnected,
right side: same rectangles now connected with glowing blue (#0070C0) and cyan (#32EDF6) lines,
unified network formation, organized and connected,
dark navy (#0E1D62) background, center vertical soft transition line,
transformation concept, clean corporate presentation style,
no text, no logos, no watermark
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, people, faces,
bright background, white, cartoon, cluttered, messy, noisy,
actual phones, actual devices, realistic objects
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.0

---

### C-12. 수익 모델 피라미드 배경 (Slide 17)

```
파일명: assets/infographics/slide17_pyramid_bg.png
슬라이드: #17 (하이브리드 수익 모델)
용도: 3단계 피라미드 인포그래픽 배경 (텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 삼각형 피라미드, 아래서 위로 갈수록 밝아지는 그라디언트
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract glowing pyramid shape on dark background, three horizontal sections,
bottom section: wide base with subtle dark blue (#0070C0) glow, solid and stable,
middle section: medium width with blue glow, growing,
top section: narrow peak with bright cyan (#32EDF6) and white glow, radiating light,
dark navy (#0E1D62) background, geometric clean pyramid structure,
upward growth and value progression concept, corporate infographic style,
subtle particle effects around pyramid, no text, no numbers, no logos, no watermark
```

**Negative Prompt:**
```
text, words, numbers, labels, logos, watermark, Egyptian pyramid,
ancient, stone, desert, bright background, white, cartoon, people,
complex details, cluttered
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.5

---

### C-13. ROI 인포그래픽 배경 (Slide 18)

```
파일명: assets/infographics/slide18_roi_bg.png
슬라이드: #18 (ROI 분석)
용도: 큰 숫자가 들어갈 4개 영역 배경 (수치/텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 4개 카드/패널이 배치될 수 있는 그리드 배경
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract dark background with four evenly spaced glowing rectangular panels,
four rounded rectangle card shapes arranged horizontally,
each panel has subtle inner glow in different shades of blue and cyan,
panel 1: blue (#0070C0) glow, panel 2: cyan (#32EDF6) glow,
panel 3: bright blue (#00B0F0) glow, panel 4: mixed blue-cyan glow,
dark navy (#0E1D62) background, subtle connecting lines between panels,
corporate KPI dashboard aesthetic, clean minimalist,
no text, no numbers, no icons, no logos, no watermark
```

**Negative Prompt:**
```
text, words, numbers, labels, logos, watermark, bright background,
white, cartoon, people, cluttered, complex, noisy, busy
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 25
- CFG: 7.0

---

### C-14. 글로벌 전략 지도 배경 (Slide 19)

```
파일명: assets/infographics/slide19_global_map_bg.png
슬라이드: #19 (글로벌 전략 & 파트너십)
용도: 세계 지도 배경 (파트너 로고/텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 글로벌 네트워크 연결 강조, C-05보다 화살표/경로 강조
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
digital world map with global network connections on dark navy background (#0E1D62),
continents formed by blue luminous dots, prominent connection arcs between
South Korea and USA, South Korea and Japan, South Korea and Europe, South Korea and China,
glowing flight path style arcs in cyan (#32EDF6),
major hub glow points at Seoul, Tokyo, New York, London, Shanghai,
global business network visualization, futuristic holographic style,
dark background, corporate presentation, no text, no labels, no country names,
no logos, no watermark
```

**Negative Prompt:**
```
text, words, labels, country names, numbers, logos, watermark,
traditional colorful map, political borders, flags, cartoon, illustration,
bright background, white, satellite photo, realistic earth
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 30
- CFG: 7.0

---

### C-15. J-Curve 차트 배경 (Slide 20)

```
파일명: assets/charts/slide20_jcurve_bg.png
슬라이드: #20 (J-Curve 로드맵)
용도: J-Curve 차트 배경 (차트는 python-pptx 생성)
크기: 1920 x 1080 px
스타일: C-04와 유사, 상승 에너지감 추가
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
dark navy blue background (#0E1D62) with subtle upward diagonal light streaks,
ascending energy visualization, soft grid lines,
gentle gradient from dark bottom-left to slightly brighter top-right,
suggests growth and upward trajectory, faint J-curve shaped light trail
in blue (#0070C0) as very subtle background element,
professional business presentation, clean and understated,
no text, no numbers, no charts, no logos, no watermark
```

**Negative Prompt:**
```
text, words, numbers, charts, graphs, actual data, logos, watermark,
bright background, white, cartoon, complex patterns, people,
cluttered, busy, colorful
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 20
- CFG: 8.0

---

### C-16. CEO/팀 슬라이드 배경 (Slide 21)

```
파일명: assets/infographics/slide21_team_bg.png
슬라이드: #21 (CEO & 팀)
용도: CEO 프로필 + 팀 구성 배경 (사진/텍스트는 오버레이)
크기: 1920 x 1080 px
스타일: 프로페셔널, 깔끔, 좌측에 사진 영역 예비
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
professional corporate profile background, dark navy (#0E1D62) gradient,
left side: subtle lighter area for photo placement, soft vignette,
right side: clean dark area with faint geometric grid pattern,
subtle blue (#0070C0) accent line separating left and right sections,
professional business card aesthetic, elegant and understated,
soft lens flare in upper area, corporate headshot background style,
no text, no people, no faces, no logos, no watermark
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, people, faces, portraits,
bright background, white, cartoon, cluttered, busy, colorful,
office interior, desk, furniture
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 20
- CFG: 7.0

---

### C-17. 타임라인 배경 (Slide 22)

```
파일명: assets/infographics/slide22_timeline_bg.png
슬라이드: #22 (국내 트랙션)
용도: 타임라인 배경 (날짜/텍스트/사진은 오버레이)
크기: 1920 x 1080 px
스타일: 수평 타임라인 흐름 배경
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
abstract horizontal timeline background, dark navy (#0E1D62) base,
single horizontal glowing line across center of image from left to right,
subtle node dots along the line at regular intervals,
line glows in gradient from blue (#0070C0) on left to bright cyan (#32EDF6) on right,
suggests progression and growth over time,
minimal and clean corporate presentation background,
soft bokeh particles near the right end,
no text, no dates, no labels, no logos, no watermark
```

**Negative Prompt:**
```
text, words, dates, numbers, labels, logos, watermark, bright background,
white, cartoon, people, complex elements, cluttered, busy, colorful
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 20
- CFG: 7.5

---

### C-18. ESG 아이콘 — Paperless (Slide 23)

```
파일명: assets/icons/slide23_esg_paperless.png
슬라이드: #23 (ESG)
용도: Paperless 아이콘 (텍스트 라벨은 오버레이)
크기: 512 x 512 px (정사각형, 투명 배경)
스타일: 플랫 아이콘, 네이비+시안 컬러
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
flat design icon, single leaf with digital circuit patterns,
paperless eco-friendly concept, leaf shape made of glowing cyan (#32EDF6) lines
on dark navy (#0E1D62) circular badge background,
no paper, green-blue sustainable technology icon,
clean vector style, centered composition, minimal,
modern corporate icon design, flat illustration,
no text, no labels, no watermark, transparent background preferred
```

**Negative Prompt:**
```
text, words, labels, watermark, realistic photograph, 3d rendering,
complex scene, people, hands, multiple objects, paper,
bright colorful background, cartoon character
```

**ComfyUI 설정:**
- Size: 512x512
- Steps: 25
- CFG: 8.0

---

### C-19. ESG 아이콘 — Food Waste Zero (Slide 23)

```
파일명: assets/icons/slide23_esg_food_waste.png
슬라이드: #23 (ESG)
용도: Food Waste Zero 아이콘
크기: 512 x 512 px
스타일: C-18과 동일한 스타일 시리즈
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
flat design icon, apple or fruit with a refresh/recycle arrow symbol,
food waste reduction concept, fruit shape with circular arrow in cyan (#32EDF6)
on dark navy (#0E1D62) circular badge background,
zero waste sustainable food icon, clean vector style, centered composition,
minimal, modern corporate icon design, flat illustration,
no text, no labels, no watermark, transparent background preferred
```

**Negative Prompt:**
```
text, words, labels, watermark, realistic photograph, 3d rendering,
complex scene, people, hands, rotten food, garbage, trash,
bright colorful background, cartoon character
```

**ComfyUI 설정:**
- Size: 512x512
- Steps: 25
- CFG: 8.0

---

### C-20. ESG 아이콘 — Social Impact (Slide 23)

```
파일명: assets/icons/slide23_esg_social.png
슬라이드: #23 (ESG)
용도: Social Impact 아이콘
크기: 512 x 512 px
스타일: C-18, C-19와 동일한 스타일 시리즈
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
flat design icon, group of connected people silhouettes forming a community,
social impact and local partnership concept,
connected human figures with handshake or heart symbol in cyan (#32EDF6)
on dark navy (#0E1D62) circular badge background,
community collaboration icon, clean vector style, centered composition,
minimal, modern corporate icon design, flat illustration,
no text, no labels, no watermark, transparent background preferred
```

**Negative Prompt:**
```
text, words, labels, watermark, realistic photograph, 3d rendering,
complex scene, detailed faces, single person,
bright colorful background, cartoon character, emoji
```

**ComfyUI 설정:**
- Size: 512x512
- Steps: 25
- CFG: 8.0

---

### C-21. 마무리 슬라이드 배경 (Slide 24)

```
파일명: assets/infographics/slide24_closing_bg.png
슬라이드: #24 (감사합니다)
용도: 깔끔한 마무리 배경 (로고+QR+연락처 오버레이)
크기: 1920 x 1080 px
스타일: 미니멀, 고급스러운 다크 네이비
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
elegant minimal dark navy (#0E1D62) background with very subtle radial gradient,
center slightly lighter than edges, very soft vignette effect,
barely visible fine geometric pattern or texture,
single subtle cyan (#32EDF6) accent line or small light flare at top center,
ultra clean, ultra minimal, professional corporate closing slide background,
luxurious understated dark theme,
no text, no logos, no icons, no watermark
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, bright, colorful, complex patterns,
people, objects, busy, cluttered, noisy, white background,
illustration, cartoon
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 15
- CFG: 8.0

---

### C-22. 부록 배경 (Slide 25)

```
파일명: assets/infographics/slide25_appendix_bg.png
슬라이드: #25 (부록)
용도: 부록 페이지 공통 배경
크기: 1920 x 1080 px
스타일: C-21보다 약간 더 밝은 변형, 텍스트 가독성 확보
```

**Nanobanana2 (SDXL) Positive Prompt:**
```
clean corporate background, dark navy blue (#0E1D62) with subtle lighter gradient
toward center, very faint horizontal line grid pattern,
slightly lighter than pure black, professional document background,
ultra minimal, suitable for dense text content,
subtle blue (#0070C0) accent at top edge,
no text, no logos, no icons, no watermark
```

**Negative Prompt:**
```
text, words, letters, logos, watermark, bright, colorful, complex,
people, objects, busy, cluttered, noisy, white, illustration, cartoon
```

**ComfyUI 설정:**
- Size: 1920x1080
- Steps: 15
- CFG: 8.0

---

## 5. Midjourney 대체 프롬프트 (Section D)

> Midjourney v6 기준. Nanobanana2 대비 더 디테일한 질감/조명 가능.
> 사용법: `/imagine prompt: [프롬프트] --ar 16:9 --v 6 --s [stylize]`
> 브랜드 컬러 적용 시: hex 코드보다 서술적 표현 사용 (MJ는 hex 미지원)

### D-01. 표지 배경 (Slide 1)

```
/imagine prompt: interior of a futuristic smart retail store, modern supermarket aisle
with glowing LED digital shelf edge displays, stretched LCD screens on every shelf rail
showing product information, deep navy blue and cyan ambient lighting, clean white shelving,
volumetric light rays, photorealistic commercial photography, wide angle 24mm lens,
shallow depth of field, 8k ultra detailed, no text, no logos --ar 16:9 --v 6 --s 250
```

### D-02. 포지셔닝 계층도 배경 (Slide 2)

```
/imagine prompt: abstract technology background, deep dark navy blue gradient fading to
midnight blue, subtle geometric layered horizontal bands with soft neon cyan glow,
connected dots and thin lines forming a hierarchy tree pattern, neural network visualization
style, soft bokeh light particles, clean minimalist corporate aesthetic,
no text, no logos --ar 16:9 --v 6 --s 200
```

### D-03. DX→AX 전환 배경 (Slide 3)

```
/imagine prompt: abstract split composition, left half monochrome gray with mechanical gears
and old circuit boards symbolizing digital automation, right half glowing deep blue and cyan
with AI neural network hologram and futuristic brain circuit symbolizing AI transformation,
smooth gradient transition in center, dark navy base, no text, no logos
--ar 16:9 --v 6 --s 200
```

### D-04. 시장 규모 차트 배경 (Slide 4)

```
/imagine prompt: minimal dark navy blue background with very subtle dotted grid lines,
faint data visualization aesthetic, soft blue glow at bottom edge, professional business
presentation slide background, nearly solid dark background with barely visible geometric
texture, no text, no numbers, no charts --ar 16:9 --v 6 --s 100
```

### D-05. 월마트 매장 (참고용) (Slide 5)

```
/imagine prompt: modern Walmart Supercenter interior, wide aisle with digital price displays,
electronic shelf labels, blue and white branding, clean retail environment,
professional retail photography, 8k --ar 16:9 --v 6 --s 150
```
> 주의: 실제 월마트 브랜드 이미지는 공식 소스에서 다운로드 권장 (Section B 참고)

### D-06. ESL 세계 지도 (Slide 6)

```
/imagine prompt: abstract world map visualization made of thousands of tiny glowing blue
and cyan dots connected by thin luminous lines, dark navy background, continents clearly
visible as dot clusters, network connections between major retail markets, highlighted
glowing nodes at USA Europe Japan South Korea China, futuristic holographic globe data
visualization, no text, no labels --ar 16:9 --v 6 --s 200
```

### D-07. AI 3-Pillar (Slide 7)

```
/imagine prompt: abstract dark navy background with three distinct vertical columns of light,
three evenly spaced illuminated pillars, left pillar cyan glow, center pillar deep blue glow,
right pillar bright blue glow, each pillar has soft light rays emanating upward,
futuristic technology aesthetic, bokeh particles floating, clean minimalist,
no text, no icons --ar 16:9 --v 6 --s 200
```

### D-08. 전용 AI vs 범용 AI (Slide 8)

```
/imagine prompt: abstract split comparison, left side blurred gray-blue digital noise with
restriction chains and limitation symbols faded, right side sharp focused glowing cyan and
blue precise technology with clean geometric shapes and power glow, dark navy background,
soft vertical dividing line in center, corporate presentation aesthetic,
no text, no logos --ar 16:9 --v 6 --s 200
```

### D-09. 데이터 흐름도 배경 (Slide 10)

```
/imagine prompt: abstract horizontal data pipeline visualization, flowing streams of blue
and cyan light particles moving left to right, four connected hub nodes along horizontal axis
with soft circular glows, dark navy background, matrix style data flow aesthetic,
network topology visualization, corporate presentation style,
no text, no labels --ar 16:9 --v 6 --s 200
```

### D-10. 3단 분산 AI 아키텍처 (Slide 11)

```
/imagine prompt: abstract three-tier horizontal architecture, bottom layer many small
scattered cyan edge device dots, middle layer medium blue access point nodes,
top layer single large bright glowing server node, dark navy background,
vertical connection lines between layers with upward flowing light particles,
hierarchical technology infrastructure visualization,
no text, no labels --ar 16:9 --v 6 --s 200
```

### D-11. 플랫폼 아키텍처 (Slide 12)

```
/imagine prompt: abstract four-layer horizontal technology stack, stacked horizontal bands
from bottom to top with increasing brightness and glow, darkest hardware base layer
to brightest AI top layer in cyan, dark navy background, soft gradient between layers,
corporate platform architecture aesthetic, clean professional,
no text, no labels --ar 16:9 --v 6 --s 150
```

### D-12. Before/After (Slide 16)

```
/imagine prompt: abstract before and after comparison, left side scattered disconnected gray
rectangles floating independently, right side same rectangles now connected with glowing
blue and cyan network lines in organized formation, dark navy background,
transformation and unification concept, corporate presentation style,
no text, no logos --ar 16:9 --v 6 --s 200
```

### D-13. 수익 피라미드 (Slide 17)

```
/imagine prompt: abstract glowing pyramid with three horizontal sections on dark navy
background, wide stable base with subtle blue glow, medium middle section with brighter
blue glow, narrow peak with radiating cyan light and sparkle effects,
upward growth and value progression, corporate infographic aesthetic,
subtle floating particles, no text, no numbers --ar 16:9 --v 6 --s 200
```

### D-14. ROI 인포그래픽 배경 (Slide 18)

```
/imagine prompt: dark navy background with four evenly spaced glowing rounded rectangular
panels arranged horizontally, each panel has subtle inner glow in different blue and cyan
shades, faint connecting lines between panels, corporate KPI dashboard aesthetic,
clean minimalist, no text, no numbers, no icons --ar 16:9 --v 6 --s 150
```

### D-15. 글로벌 전략 지도 (Slide 19)

```
/imagine prompt: digital world map with prominent glowing flight path arcs connecting
South Korea to USA Japan and Europe, continents as blue luminous dot clusters on dark
navy background, major hub cities have bright cyan glow points, global business network
visualization, holographic style, no text, no labels,
no country names --ar 16:9 --v 6 --s 200
```

### D-16. J-Curve 차트 배경 (Slide 20)

```
/imagine prompt: dark navy blue background with subtle upward diagonal light streaks
suggesting growth, faint grid lines, gentle gradient brighter toward upper right,
very subtle J-curve shaped light trail in deep blue, professional business presentation
background, clean understated, no text, no numbers, no charts --ar 16:9 --v 6 --s 100
```

### D-17. CEO/팀 배경 (Slide 21)

```
/imagine prompt: professional corporate profile background, dark navy gradient,
left side slightly lighter area for photo placement with soft vignette,
right side clean dark area with faint geometric grid, subtle blue accent line divider,
elegant understated executive portrait background, soft lens flare,
no text, no people, no faces --ar 16:9 --v 6 --s 150
```

### D-18. 타임라인 배경 (Slide 22)

```
/imagine prompt: abstract horizontal timeline visualization, dark navy background,
single glowing horizontal line across center from left to right, subtle node dots along
the line at regular intervals, line color gradient from deep blue on left to bright cyan
on right suggesting progression, minimal corporate presentation background,
soft bokeh at right end, no text, no dates --ar 16:9 --v 6 --s 150
```

### D-19. ESG 아이콘 — Paperless (Slide 23)

```
/imagine prompt: flat design icon, single leaf with embedded digital circuit pattern lines,
paperless eco-tech concept, cyan glowing leaf on dark navy circular badge, clean vector style,
centered, minimal modern corporate icon, no text --ar 1:1 --v 6 --s 200
```

### D-20. ESG 아이콘 — Food Waste Zero (Slide 23)

```
/imagine prompt: flat design icon, apple fruit with circular recycle arrow symbol,
food waste reduction concept, cyan glowing fruit and arrow on dark navy circular badge,
clean vector style, centered, minimal modern corporate icon, no text --ar 1:1 --v 6 --s 200
```

### D-21. ESG 아이콘 — Social Impact (Slide 23)

```
/imagine prompt: flat design icon, group of connected human silhouettes forming community
with handshake symbol, social impact concept, cyan glowing figures on dark navy circular badge,
clean vector style, centered, minimal modern corporate icon, no text --ar 1:1 --v 6 --s 200
```

### D-22. 마무리 배경 (Slide 24)

```
/imagine prompt: ultra minimal elegant dark navy background with very subtle radial gradient,
center slightly lighter, fine barely visible geometric texture, single tiny cyan accent
light flare at top center, luxurious understated professional closing slide,
no text, no logos --ar 16:9 --v 6 --s 50
```

### D-23. 부록 배경 (Slide 25)

```
/imagine prompt: clean minimal dark navy blue corporate background with faint horizontal
grid lines, subtle lighter gradient toward center for text readability, very subtle blue
accent at top edge, professional document background for dense text,
no text, no logos --ar 16:9 --v 6 --s 50
```

---

## 6. python-pptx 차트 (참고)

> 아래 차트는 이미지 생성이 아닌 python-pptx 스크립트로 직접 생성.
> 배경 이미지(C-04, C-15)와 조합하여 사용.
> 상세 데이터: `docs/references/market_data.md`

| # | 차트 유형 | 슬라이드 | 데이터 | 배경 이미지 |
|---|----------|---------|--------|-----------|
| 1 | 막대 그래프 | #4 | ESL 시장 2022~2030 ($1.29B~$8.37B) | C-04 |
| 2 | 라인 그래프 | #4 | RMN 광고비 2022~2030 ($114.6B~$312B) | C-04 |
| 3 | 라인 그래프 | #4 | AI in Retail 2022~2030 ($5.5B~$40.74B) | C-04 |
| 4 | 막대 그래프 | #5 | Walmart Connect FY2021~FY2025 ($2.1B~$6.4B) | 별도 배경 불필요 |
| 5 | 테이블 | #6 | ESL 지역별 도입률 (미/일/유/한/기타) | C-05 |
| 6 | J-Curve 그래프 | #20 | 매출 로드맵 2025~2030 (30억~2,000억) | C-15 |

**차트 스타일 가이드:**
- 배경색: Dark Navy `#0E1D62`
- 막대/라인 컬러: Cyan `#32EDF6`, Blue `#0070C0`, Bright Blue `#00B0F0`
- 텍스트 컬러: White `#FFFFFF`
- 폰트: Pretendard 또는 Noto Sans KR
- 출처 텍스트: 10pt, Light Gray `#999999`, 우하단

---

## 7. QR 코드 생성

> Slide 24용. Python `qrcode` 라이브러리로 생성 가능.
> 스타일: 브랜드 컬러 적용한 커스텀 QR

| # | URL | 라벨 | 저장 경로 | 스타일 |
|---|-----|------|----------|--------|
| 1 | `https://www.aisirius.ai` | 회사 홈페이지 | `assets/images/qr_homepage.png` | 네이비 배경 + 시안 모듈 |
| 2 | `https://cms.aisirius.ai` | CMS 데모 | `assets/images/qr_cms.png` | 네이비 배경 + 블루 모듈 |
| 3 | `https://mt.aisirius.ai` | 회의실 시스템 | `assets/images/qr_meeting.png` | 네이비 배경 + 브라이트 블루 모듈 |

**생성 스크립트 (참고):**
```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask

qr = qrcode.QRCode(version=1, box_size=20, border=2)
qr.add_data("https://www.aisirius.ai")
qr.make(fit=True)
img = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SolidFillColorMask(
        back_color=(14, 29, 98),      # #0E1D62
        front_color=(50, 237, 246)     # #32EDF6
    )
)
img.save("assets/images/qr_homepage.png")
```

---

## 부록: 이미지 생성 우선순위

### Priority 1 — Essential (5분 발표 핵심)

| 순서 | 이미지 ID | 슬라이드 | 설명 |
|------|----------|---------|------|
| 1 | C-01 | #1 | 표지 배경 |
| 2 | A-01 | #1, #24 | 로고 (기존) |
| 3 | C-06 | #7 | AI 3-pillar 배경 |
| 4 | C-07 | #8 | 전용 vs 범용 AI 배경 |
| 5 | C-12 | #17 | 수익 피라미드 배경 |
| 6 | C-15 | #20 | J-Curve 배경 |
| 7 | C-21 | #24 | 마무리 배경 |

### Priority 2 — Standard (15분 발표 추가)

| 순서 | 이미지 ID | 슬라이드 | 설명 |
|------|----------|---------|------|
| 8 | C-03 | #3 | DX→AX 배경 |
| 9 | B-02 | #5 | 월마트 로고/참조 |
| 10 | A-03 | #9, #13 | CMS 스크린샷 (기존) |
| 11 | C-09 | #11 | 3단 분산 AI 배경 |
| 12 | C-10 | #12 | 플랫폼 아키텍처 배경 |
| 13 | C-14 | #19 | 글로벌 전략 지도 |
| 14 | B-01 | #19 | 파트너 로고 다운로드 |
| 15 | A-05 | #21 | CEO 사진 (기존) |
| 16 | A-06 | #22 | 트랙션 사진 (기존) |

### Priority 3 — Expandable (30분 발표 추가)

| 순서 | 이미지 ID | 슬라이드 | 설명 |
|------|----------|---------|------|
| 17 | C-05 | #6 | ESL 세계 지도 |
| 18 | C-08 | #10 | 데이터 흐름도 배경 |
| 19 | A-02 | #14, #15 | 디바이스 사진 (기존) |
| 20 | C-11 | #16 | Before/After 배경 |
| 21 | C-13 | #18 | ROI 인포그래픽 배경 |
| 22 | C-18~20 | #23 | ESG 아이콘 3종 |
| 23 | C-22 | #25 | 부록 배경 |

---

## 체크리스트

- [ ] 기존 이미지 470개에서 해당 파일 탐색 및 `assets/` 복사
- [ ] 파트너사 로고 공식 소스에서 다운로드
- [ ] Nanobanana2 Priority 1 이미지 생성 (7개)
- [ ] Nanobanana2 Priority 2 이미지 생성 (추가 5개)
- [ ] Nanobanana2 Priority 3 이미지 생성 (추가 6개)
- [ ] QR 코드 3개 생성
- [ ] python-pptx 차트 6개 스크립트 준비
- [ ] 모든 이미지 `assets/` 하위 폴더에 정리 완료
- [ ] 이미지 해상도/비율 최종 확인

---

> **작성자**: Claude Code
> **최종 수정**: 2026-03-02
> **다음 작업**: Priority 1 이미지부터 순차 생성, 기존 이미지 탐색/분류 병행
