# IRdeck 작업일지

> 집/회사 양쪽에서 작업하므로, 세션 전환 시 이 문서를 참조하여 진행 상황을 파악합니다.

---

## 2026-03-01 (토) - 프로젝트 초기 세팅

### 완료 항목
1. **기존 문서 전수 분석**
   - `G:\00.googledrive\07.AIsirius\20.회사소개서\` 내 ~70개 문서 분석
   - 5개 고유 콘텐츠 계열로 압축 (IR Deck, 파트너소개, CMS소개, AI ISM, 투자요약)
   - 최신 문서 6개 텍스트 추출 완료 (PPTX: python-pptx, DOCX: python-docx)

2. **소구 포인트 정리**
   - 20개 소구 포인트 → AI 중심 5-Tier 구조로 재편
   - CEO 방향성 반영: "리테일 전문 AI" 포지셔닝 확정
   - 기존 문서 대비 강조 포인트 조정 테이블 작성

3. **특허 분석**
   - 출원 특허: 멀티모달 3단계 분산 AI 처리 시스템 (10-2025-0208402) 상세 분석
   - 등록 특허: 배터리 충전 장치 2건 (10-2303197, 10-2331690) 확인
   - 특허 소스: `G:\00-1.googledrive\07.Cilinus\10.경영\06.특허\`

4. **프로젝트 폴더 구조 생성**
   - `G:\30.dev\IRdeck\` 전체 디렉토리 구조 생성
   - CLAUDE.md, 스킬 3개, 커맨드 1개, settings.local.json 생성

5. **디바이스 스펙 기록**
   - Stretched LCD 23" (60x6cm, 1920x158)
   - Stretched LCD 29" (70x23cm, 1920x540)
   - 목록 계속 추가 예정

### 핵심 결정 사항
- **포지셔닝**: AIsirius = 리테일 전문 AI 기업 (AI가 핵심)
- **RMN이 메인**, ESL은 RMN에 내장된 기능
- **기존 Android 기기 SW 설치만으로 생태계 흡수** 가능 (핵심 차별점)
- **HW는 중국 파트너사 소싱** (자체 개발 아님)
- AI = 콘텐츠 생성 + POS 연동 플래노그램 분석 + AI 제안

### 다음 작업 (TODO)
- [ ] 슬라이드 구조 설계 (어떤 문서부터? 투자제안서 or 회사소개서)
- [ ] 슬라이드별 콘텐츠 원고 작성 (`docs/content/`)
- [ ] PPTX 템플릿 설계/선정
- [ ] 나노바나나2 이미지/인포그래픽 생성 시작
- [ ] 디바이스 목록 추가 (CEO 제공 대기)
- [ ] python-pptx 빌드 스크립트 개발

---

## 2026-03-01 (토) - 세션 2: 추가 분석 및 프로세스 구축

### 완료 항목
1. **Notion 시연 시나리오 분석** (26년 2월 인탑스/DK/정훈 시연)
   - CMS 핵심 기능 9가지 실증 내용 추출
   - 데이터 기반 콘텐츠 관리, 실시간 태그/상품 관리, 크로스 디바이스 연동 등
   - `docs/analysis/문서분석_전체요약.md` 섹션 3-1에 반영

2. **CMS 매뉴얼 및 Cilinus 리포지토리 탐색**
   - AI 모델 통합 (Z-image, Wan, Flux.2, Qwen + LoRA), 해상도 자동 적응 등
   - 파트너사 25개+, 영업 파이프라인, 정부 사업 5건 확인
   - `docs/analysis/문서분석_전체요약.md` 섹션 3-2에 반영

3. **범용 AI vs 전용 AI 비교 테이블 작성**
   - 저작권/사용권, 크기/해상도/비율 제한, 동영상 생성 시간 차이
   - 자체 전용 AI 서버 구축 사실 반영

4. **워터마크 → PDF → 암호 자동화 프로세스 구축**
   - `scripts/watermark_pdf.py` 생성
   - 로고만 주면 자동으로 반투명 워터마크 생성 → PPTX 삽입 → PDF 변환 → 암호(옵션)
   - 워터마크 PPTX는 업체별 커스텀 가능하도록 영구 저장
   - `docs/references/watermark_pdf_process.md` 프로세스 문서 작성

5. **글로벌 시장 규모 연도별 데이터 정리**
   - ESL, RMN, 디지털 사이니지, AI in Retail, 월마트 커넥트 — 5개 시장
   - 2022~2030 연도별 USD/KRW + 출처 + python 차트용 데이터
   - `docs/references/market_data.md` 생성

6. **서비스 URL 업데이트**
   - cms.aisirius.ai, epd.aisirius.ai, mt.aisirius.ai
   - AI 서버: 121.165.20.68:8188 (ComfyUI)
   - `docs/credentials.md` 업데이트

7. **집/회사 경로 구분**
   - CLAUDE.md에 집(Home)/회사(Office) 별 참조 폴더 경로 테이블 추가
   - 회사 PC 경로는 첫 작업 시 확인 필요

### 핵심 추가 사항
- **전용 AI 서버**: 회사 자체 구축, ComfyUI 기반
- **범용 AI 제한**: 저작권(제품 이미지 불가), 비정형 해상도 불가, 동영상 길이 제한
- **전용 AI 강점**: 매장 사용권, 비정형 stretched LCD 대응, 지속적 학습/튜닝

### 다음 작업 (TODO)
- [ ] 회사소개서 슬라이드 구조 설계 및 승인
- [ ] 슬라이드별 콘텐츠 원고 작성 (`docs/content/`)
- [ ] PPTX 템플릿 설계/선정
- [ ] 나노바나나2 이미지/인포그래픽 생성 시작
- [ ] 디바이스 목록 추가 (CEO 제공 대기)
- [ ] python-pptx 빌드 스크립트 개발
- [ ] Google Calendar MCP 설정 (jyk@aisirius.ai)
- [ ] 회사 PC 경로 확인 및 CLAUDE.md 업데이트

---

## 2026-03-01 (토) - 세션 3: 슬라이드 구조 설계 및 2버전 콘텐츠 작성

### 완료 항목
1. **회사소개서 슬라이드 구조 설계** (25장, 6개 파트)
   - `docs/content/회사소개서_슬라이드구조.md` 생성
   - Part 1~6: 오프닝(2장) → 시장기회(4장) → AI핵심(5장) → 플랫폼(5장) → 비즈니스(4장) → 팀/마무리(5장)
   - 대상별 커스텀 가이드 (투자자/파트너/고객)
   - 나노바나나2 이미지 목록 14개, python-pptx 차트 목록 6개 정리

2. **Version A (비주얼형) 세부내용 작성** (25장)
   - `docs/content/슬라이드_세부내용_VerA_비주얼.md`
   - 인포그래픽/이미지 중심, 키워드 위주 텍스트
   - 파트너사/고객사 대상

3. **Version B (텍스트 상세형) 세부내용 작성** (28장, 646줄)
   - `docs/content/슬라이드_세부내용_VerB_텍스트상세.md`
   - CEO 작성 스타일 분석: `AIsirius_ 소개자료_신세계inc_20260226.pptx` (21장)
     - 14pt 본문, Bold 강조, 영한 혼용, 뉴스 기사 원문 인용, 번호 리스트+상세 설명
   - CEO 선호 스타일 반영: 풀 문장 설명 + 데이터 근거 + 뉴스 인용
   - 투자자/대표 선호/상세 설명 대상

### 핵심 결정 사항
- **2버전 병행 전략**: Version A(비주얼) + Version B(텍스트 상세) 동시 관리
- **CEO 스타일**: 텍스트 중심, Bold 강조, 영한 혼용 (신세계inc 문서 기반 확인)

### 다음 작업 (TODO)
- [x] ~~PPTX 템플릿 설계/선정~~ → 세션 4에서 완료
- [x] ~~python-pptx 빌드 스크립트 개발~~ → 세션 4에서 완료
- [x] ~~python-pptx 차트 코드 작성~~ → 세션 4에서 완료
- [ ] 나노바나나2 이미지/인포그래픽 생성 시작
- [ ] 디바이스 목록 추가 (CEO 제공 대기)
- [ ] Google Calendar MCP 설정 (jyk@aisirius.ai)
- [ ] 회사 PC 경로 확인 및 CLAUDE.md 업데이트

---

## 2026-03-01 (토) - 세션 4: PPTX 빌드 파이프라인 구축

### 완료 항목
1. **CEO 프레젠테이션 디자인 분석** (신세계inc_20260226.pptx)
   - 16:9, 14개 브랜드 컬러 팔레트 추출
   - 폰트: 에스코어 드림/맑은 고딕/Arial, 크기 10~44pt
   - 크롬: 오각형 헤더바 + 3색 푸터바 + 분리선 + 우상단 로고
   - 전체 파일 77개 중 3개 상세 분석

2. **scripts/components/ 패키지 생성** (7개 모듈)
   - `colors.py` — 14개 브랜드 컬러 RGBColor 상수
   - `fonts.py` — 폰트 역할 설정 + apply_font() (East Asian/Latin XML 동시 설정)
   - `layouts.py` — 좌표 상수 + LayoutType 열거형 18종
   - `chrome.py` — 헤더바/푸터/분리선/로고/슬라이드번호 함수
   - `charts.py` — 시장 데이터 차트 5종 + 도입률 테이블
   - `markdown_parser.py` — 마크다운 → SlideContent 데이터클래스 파싱

3. **scripts/create_templates.py** 생성
   - 16:9 빈 템플릿 2개 자동 생성 (A/B)
   - `templates/aisirius_template_A.pptx`, `templates/aisirius_template_B.pptx`

4. **scripts/build_deck.py** 메인 빌더 생성
   - CLI: `python scripts/build_deck.py --version A|B|all [--watermark --company "회사명"]`
   - 마크다운 파싱 → 슬라이드별 레이아웃 디스패치 → PPTX 생성
   - 10종 레이아웃 빌더: title_cover, two_column, chart_slide, chart_detailed, text_heavy, comparison_table, three_pillar, news_quote, infographic_numbers, thank_you
   - 이미지 미존재 시 플레이스홀더 사각형 표시

5. **통합 테스트 완료**
   - Version A: 25장, 287 shapes, 차트 3장(#4,5,20), 테이블 1장(#6)
   - Version B: 26장, 242 shapes, 차트 4장(#4,5,7,20), 테이블 3장(#18,19,22)
   - 출력: `output/회사소개서/AIsirius_회사소개서_VerA_20260301.pptx` (111KB)
   - 출력: `output/회사소개서/AIsirius_회사소개서_VerB_20260301.pptx` (112KB)

### 핵심 기술 결정
- **프로그래밍으로 템플릿 생성** (PowerPoint 수동 작업 불필요)
- **크롬은 per-slide 추가** (표지/감사 슬라이드 제외)
- **python-pptx 네이티브 차트** → PowerPoint에서 편집 가능
- **Bold 마크다운 렌더링** — `**text**` 패턴을 bold run으로 변환

### 다음 작업 (TODO)
- [ ] PPTX 시각 검토 후 레이아웃 조정
- [ ] 나노바나나2 이미지/인포그래픽 생성 → 플레이스홀더 교체
- [ ] 디바이스 목록 추가 (CEO 제공 대기)
- [ ] Google Calendar MCP 설정 (jyk@aisirius.ai)
- [ ] 회사 PC 경로 확인 및 CLAUDE.md 업데이트

---

## 주요 파일 위치 (빠른 참조)
| 파일 | 위치 |
|------|------|
| 소구 포인트 정리 | `docs/analysis/문서분석_전체요약.md` |
| 프로젝트 가이드 | `CLAUDE.md` |
| 이 작업일지 | `docs/worklog.md` |
| 슬라이드 구조 | `docs/content/회사소개서_슬라이드구조.md` |
| 슬라이드 Ver.A (비주얼) | `docs/content/슬라이드_세부내용_VerA_비주얼.md` |
| 슬라이드 Ver.B (텍스트) | `docs/content/슬라이드_세부내용_VerB_텍스트상세.md` |
| 시장 규모 데이터 | `docs/references/market_data.md` |
| 워터마크 프로세스 | `docs/references/watermark_pdf_process.md` |
| 워터마크 스크립트 | `scripts/watermark_pdf.py` |
| 계정/URL 정보 | `docs/credentials.md` |
| 기존 문서 원본 | `G:\00.googledrive\07.AIsirius\20.회사소개서\` |
| 특허 문서 | `G:\00-1.googledrive\07.Cilinus\10.경영\06.특허\` |
| 메모리 | `C:\Users\frogm\.claude\projects\g--30-dev-IRdeck\memory\MEMORY.md` |
