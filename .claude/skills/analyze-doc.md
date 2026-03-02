# 문서 분석 스킬

기존 PPT, DOCX, PDF 문서를 분석하여 소구 포인트를 추출합니다.

## 사용법
`/analyze-doc [파일경로]`

## 동작
1. 문서 텍스트 추출:
   - PPTX: python-pptx 또는 `python -m markitdown file.pptx`
   - DOCX: python-docx
   - PDF: PyPDF2 또는 pikepdf
2. 슬라이드/페이지별 핵심 내용 요약
3. 소구 포인트 카테고리별 분류:
   - 시장 기회 (Market Opportunity)
   - 비즈니스 모델 (Business Model)
   - 핵심 기술 (Core Technology) — AI 역량 최우선
   - 성과/레퍼런스 (Traction)
   - 재무/투자 (Finance & Investment)
   - 팀/회사 (Team & Company)
   - ESG 경영
4. 기존 분석(`docs/analysis/문서분석_전체요약.md`)과 중복 여부 체크
5. 결과를 `docs/analysis/`에 저장

## 소스 문서 경로 (집)
- 기존 문서: `G:\00.googledrive\07.AIsirius\20.회사소개서\`
- 특허 문서: `G:\00-1.googledrive\07.Cilinus\10.경영\06.특허\`
- CMS 매뉴얼: `G:\00-1.googledrive\07.Cilinus\30.Dev\10.기획\`

## 출력 형식
```markdown
## [파일명] 분석 결과
### 신규 소구 포인트
- [카테고리] 내용 ...
### 기존 대비 업데이트된 내용
- [카테고리] 기존 → 변경 ...
### 중복 (skip)
- ...
```

## 연계 스킬
- `/update-content` — 분석 결과를 슬라이드 콘텐츠에 반영
- `/build-deck` — 업데이트된 콘텐츠로 PPTX 빌드
