# /review-design 커맨드

생성된 PPTX의 디자인 품질을 검증합니다.

## 사용법
```
/review-design [파일경로]              # 특정 파일 리뷰
/review-design output/회사소개서/      # 디렉토리 전체 리뷰
```

## 리뷰 프로세스

### 1. 구조 분석
- python-pptx로 슬라이드별 shape 수, 텍스트 길이, 차트/테이블 유무 추출
- 레이아웃 타입별 요소 배치 검증

### 2. 디자인 원칙 체크 (CRAP)
참조: `.agents/skills/graphic-designer/SKILL.md`
- **Contrast**: 제목-본문 크기 대비 2배 이상?
- **Repetition**: 크롬 요소(헤더/푸터/로고) 일관성?
- **Alignment**: 텍스트 박스 정렬 통일?
- **Proximity**: 관련 요소 그룹핑?

### 3. 프레젠테이션 진단
참조: `.agents/skills/presentation-design/SKILL.md`
- 청중 중심 설계?
- Assertion-Evidence 구조?
- 슬라이드당 1 메시지?
- 인지 부하 적정?

### 4. 브랜드 준수
참조: `.claude/rules/brand-guidelines.md`
- 14색 브랜드 컬러 준수?
- 폰트 가이드라인 준수?
- 슬라이드 규격 (16:9)?

### 5. Ver.A/B 일관성
- 양 버전 내용 동일 확인
- 슬라이드 수 차이 검증

## 출력
```markdown
## 디자인 리뷰: [파일명]
### 점수 요약 (100점 만점)
| 항목 | 점수 | 상태 |
|------|------|------|
| 시각적 계층 | xx/25 | ✅/⚠️/❌ |
| 인지 부하 | xx/25 | ✅/⚠️/❌ |
| 브랜드 일관성 | xx/25 | ✅/⚠️/❌ |
| 콘텐츠 정합성 | xx/25 | ✅/⚠️/❌ |

### 개선 필요 사항
1. [Critical] ...
2. [Important] ...
3. [Nice-to-have] ...
```
