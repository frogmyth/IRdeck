# IRdeck - AIsirius IR/투자제안서/회사소개서 자동 생성 프로젝트

## 프로젝트 개요
AIsirius(에이아이시리우스)의 투자제안서, 회사소개서, 파트너 제안서를 효율적으로 생성/관리하는 프로젝트.
기존 PPT/DOCX 문서를 분석하여 소구 포인트를 추출하고, python-pptx를 활용하여 PPTX를 자동 생성한다.

## 회사 정보
- **회사명**: 에이아이시리우스(주) (AIsirius Co., Ltd.) - 전 Cilinus
- **핵심 포지셔닝**: 리테일 전문 AI 기업 (AI가 핵심, 플랫폼은 적용 무대)
- **사업**: AI 기반 리테일 미디어 플랫폼 (RMN + ESL 통합)
- **CEO**: 김현학 (삼성전기 ESL 출신, ESL 2~4세대 세계 최초 개발)
- **연락처**: sale@aisirius.ai / 031-360-7869
- **소재지**: 경기도 수원시 영통구 광교로 105, 경기R&DB센터 709호

## 작업 환경
- **집/회사 양쪽에서 작업** — 세션 전환 시 작업일지 참조
- 작업일지: `docs/worklog.md`
- 메모리: `C:\Users\frogm\.claude\projects\g--30-dev-IRdeck\memory\MEMORY.md`
- 계정/URL 정보: `docs/credentials.md` (민감 정보 — git 제외 대상)

## 특허 현황
- **출원**: 멀티모달 3단계 분산 AI 시스템 (10-2025-0208402) — 엣지→AP→서버 자율 분기
- **등록**: 배터리 충전 장치 2건 (10-2303197, 10-2331690)
- 특허 소스: `G:\00-1.googledrive\07.Cilinus\10.경영\06.특허\`

## 폴더 구조
```
IRdeck/
├── CLAUDE.md                          # 프로젝트 가이드
├── .claude/
│   ├── skills/                        # Claude 스킬
│   │   ├── analyze-doc.md             # 문서 분석 스킬
│   │   ├── generate-pptx.md           # PPTX 생성 스킬
│   │   └── update-content.md          # 콘텐츠 업데이트 스킬
│   ├── commands/                      # 커스텀 커맨드
│   │   └── build-deck.md              # 덱 빌드 커맨드
│   └── settings.local.json
├── docs/
│   ├── analysis/                      # 기존 문서 분석 결과
│   │   └── 문서분석_전체요약.md        # 전체 소구 포인트 정리
│   ├── content/                       # 슬라이드별 콘텐츠 원고
│   ├── references/                    # 참고 자료 (시장 데이터 등)
│   ├── worklog.md                     # 작업일지 (집/회사 세션 전환용)
│   └── credentials.md                 # URL/계정 정보 (민감정보)
├── templates/                         # PPTX 템플릿
├── assets/
│   ├── images/                        # 일반 이미지 (제품, 매장 사진 등)
│   ├── infographics/                  # 인포그래픽 (텍스트 분리형)
│   ├── charts/                        # 도표/차트
│   └── icons/                         # 아이콘
├── output/                            # 생성된 최종 PPTX
│   ├── 투자제안서/
│   ├── 회사소개서/
│   └── 파트너제안서/
└── scripts/                           # PPTX 생성 Python 스크립트
```

## 기술 스택
- **문서 처리**: python-pptx, python-docx, PyPDF2
- **이미지/인포그래픽**: 나노바나나2 (Nanobanana2) 연동
- **AI 콘텐츠**: Claude Code (텍스트 작성/구조화)

## 이미지 처리 규칙
1. **인포그래픽 텍스트**: 이미지와 분리하여 수정 가능하도록 구현
   - 배경/도형 = 이미지(나노바나나2)
   - 텍스트 = python-pptx의 텍스트 레이어로 별도 오버레이
2. **이미지 내 텍스트**: 원근감이 적용된 텍스트는 이미지에 포함하여 생성
   - 나노바나나2에서 텍스트가 포함된 완성 이미지로 생성

## 워크플로우
1. 기존 문서 분석 → `docs/analysis/`에 소구 포인트 정리
2. 슬라이드 구조 설계 → `docs/content/`에 원고 작성
3. 이미지/인포그래픽 생성 → `assets/`에 저장
4. PPTX 템플릿 적용 → `templates/`
5. 최종 PPTX 빌드 → `output/`에 출력

## 소스 문서 위치 (집/회사 경로 구분)

### 집 (Home)
| 항목 | 경로 |
|------|------|
| 프로젝트 루트 | `G:\30.dev\IRdeck\` |
| 기존 문서 | `G:\00.googledrive\07.AIsirius\20.회사소개서\` |
| 이미지 소스 | `G:\00.googledrive\07.AIsirius\20.회사소개서\images\` |
| 회사 문서 전체 | `G:\00-1.googledrive\07.Cilinus\` |
| 특허 문서 | `G:\00-1.googledrive\07.Cilinus\10.경영\06.특허\` |
| CMS 매뉴얼 | `G:\00-1.googledrive\07.Cilinus\30.Dev\10.기획\` |
| 메모리 | `C:\Users\frogm\.claude\projects\g--30-dev-IRdeck\memory\MEMORY.md` |

### 회사 (Office)
| 항목 | 경로 |
|------|------|
| 프로젝트 루트 | (확인 필요 — 회사 PC 세팅 시 기록) |
| 기존 문서 | (Google Drive 동기화 경로 확인 필요) |
| 이미지 소스 | (상동) |
| 회사 문서 전체 | (상동) |
| 특허 문서 | (상동) |
| CMS 매뉴얼 | (상동) |
| 메모리 | (회사 PC의 사용자 폴더 확인 필요) |

> **참고**: 회사 PC에서 처음 작업 시 위 경로를 확인하여 업데이트해주세요.
> Google Drive 동기화 폴더 위치가 다를 수 있습니다.

## 주의사항
- 한국어와 영문이 혼용되는 문서임. 기본은 한국어 기준.
- 대상별 커스텀 버전 생성 필요 (투자자, 파트너사, 고객사)
- .pen 파일은 pencil MCP 도구로만 접근
- 기밀 정보(투자 조건, 주식 현황 등)는 버전별 관리
- URL/계정 정보는 `docs/credentials.md`에 기록
