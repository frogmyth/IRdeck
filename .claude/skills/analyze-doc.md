# 문서 분석 스킬

기존 PPT, DOCX, PDF 문서를 분석하여 소구 포인트를 추출합니다.

## 사용법
`/analyze-doc [파일경로]`

## 동작
1. python-pptx 또는 python-docx로 문서 텍스트 추출
2. 슬라이드/페이지별 핵심 내용 요약
3. 소구 포인트 카테고리별 분류:
   - 시장 기회 (Market Opportunity)
   - 비즈니스 모델 (Business Model)
   - 핵심 기술 (Core Technology)
   - 성과/레퍼런스 (Traction)
   - 재무/투자 (Finance & Investment)
   - 팀/회사 (Team & Company)
4. 기존 분석과 중복 여부 체크
5. 결과를 `docs/analysis/`에 저장

## 출력 형식
```markdown
## [파일명] 분석 결과
### 신규 소구 포인트
- ...
### 기존 대비 업데이트된 내용
- ...
### 중복 (skip)
- ...
```
