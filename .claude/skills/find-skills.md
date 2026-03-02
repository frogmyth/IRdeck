# 스킬 검색 스킬

커뮤니티 에이전트 스킬 생태계에서 필요한 스킬을 검색하고 설치합니다.

## 사용법
`/find-skills [검색어]`

## 주요 명령어
```bash
npx skills find [query]    # 스킬 검색
npx skills add <package>   # 스킬 설치
npx skills add <pkg> -y    # 확인 없이 설치
npx skills check           # 업데이트 확인
npx skills update          # 전체 업데이트
```

## 검색 팁
| 카테고리 | 검색어 예시 |
|----------|------------|
| 프레젠테이션 | presentation, slides, pptx |
| 디자인 | design, ui, graphic, layout |
| 문서 | document, writing, docs |
| 코드 품질 | review, lint, refactor |
| 배포 | deploy, docker, ci-cd |

## 설치 위치
- 프로젝트 로컬: `.agents/skills/[스킬명]/`
- 글로벌: `-g` 플래그 사용

## 현재 설치된 커뮤니티 스킬
- `presentation-design` — 프레젠테이션 디자인 평가/진단 (jwynia)
- `graphic-designer` — 그래픽 디자인 원칙 (thepexcel)
- `pptx` — PPTX 생성/편집/분석 워크플로우 (rysweet)

## 참고
- 스킬 브라우저: https://skills.sh/
- 설치 전 내용 검토 권장 (에이전트 권한으로 실행됨)
