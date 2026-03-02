# PPTX 생성 스킬

python-pptx를 사용하여 투자제안서/회사소개서 PPTX를 자동 생성합니다.

## 사용법
`/generate-pptx [유형] [대상]`
- 유형: ir-deck | company-intro | partner-proposal | cms-intro
- 대상: general | [회사명] (예: tcs, nri, 신세계)

## 동작
1. `docs/content/` 디렉토리에서 해당 유형의 콘텐츠 원고 로드
2. `scripts/components/markdown_parser.py`로 Markdown → SlideContent 파싱
3. `templates/` 디렉토리에서 PPTX 템플릿 로드
4. `assets/` 디렉토리에서 이미지/인포그래픽 매핑
5. `scripts/build_deck.py`로 PPTX 빌드:
   - 브랜드 컴포넌트 적용 (colors, fonts, chrome, charts)
   - 18종 레이아웃 타입별 빌더 사용
   - 텍스트 배치 (한글/영문 동시 폰트 설정)
6. 대상별 커스텀 처리:
   - 회사명/로고 삽입
   - 기밀 정보 필터링
   - 워터마크 적용 (필요시 `scripts/watermark_pdf.py`)
7. `output/[유형]/` 디렉토리에 저장

## 빌드 명령어
```bash
python scripts/build_deck.py --version A              # Ver.A 비주얼 (새 파일)
python scripts/build_deck.py --version B              # Ver.B 텍스트상세 (새 파일)
python scripts/build_deck.py --version all            # 전체 (새 파일)
python scripts/build_deck.py --version A --overwrite  # 오류 수정 시 덮어쓰기
python scripts/build_deck.py --version A --watermark --company "대상사"
```

## 텍스트 상자 규칙
- 자동 맞춤: `MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT` (도형을 텍스트 크기에 맞춤)
- 자동 줄바꿈 OFF: `tf.word_wrap = False`
- 줄바꿈은 명시적 Enter(새 문단)으로만 처리
- `_wrap_text_to_lines()` 함수가 박스 너비 기준으로 자동 줄바꿈 계산

## 이미지 처리 규칙
- **가로세로 비율 변경 금지** — 축소/확대 후 안 되면 크롭
- `_add_picture_fit()`: 비율 유지 + 크롭으로 영역에 맞춰 배치
- 인포그래픽 텍스트 → python-pptx 텍스트 박스로 오버레이 (수정 가능)
- 원근감 적용 텍스트 → 이미지 내 포함 (나노바나나2로 생성)
- 차트/도표 → python-pptx 차트 객체 (MARKET_DATA 딕셔너리 참조)
- 이미지 소스: `assets/images/slides/` (CEO PPT 추출 + 회사소개서 폴더)

## 파일 버전 관리
- 오류 수정 → `--overwrite` (기존 파일 덮어쓰기)
- 내용/디자인 변경 → 새 순번 파일 (`_YYYYMMDD_NN.pptx`)
- Ver.A / Ver.B 별도 순번

## 디자인 참고
- `.claude/rules/brand-guidelines.md` — 브랜드 컬러/폰트
- `.claude/rules/presentation-rules.md` — 슬라이드 디자인 가이드
- `.agents/skills/graphic-designer/` — CRAP 원칙, 디자인 체크리스트
- `.agents/skills/pptx/` — PPTX 생성 고급 워크플로우 (html2pptx, ooxml)

## 출력
- `output/[유형]/AIsirius_[유형]_[대상]_[날짜].pptx`
