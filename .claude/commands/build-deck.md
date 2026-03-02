# /build-deck 커맨드

투자제안서/회사소개서 PPTX를 빌드합니다.

## 사용법
```
/build-deck ir [대상명]       # IR 투자제안서
/build-deck intro [대상명]    # 회사소개서
/build-deck partner [대상명]  # 파트너 제안서
/build-deck cms              # CMS 소개서
```

## 빌드 프로세스
1. 콘텐츠 원고 검증 (`docs/content/`)
2. 에셋 검증 (`assets/`)
3. 템플릿 로드 (`templates/`)
4. python-pptx 빌드 (`scripts/build_deck.py`)
5. 출력 (`output/`)
6. (선택) 워터마크 PDF 생성 (`scripts/watermark_pdf.py`)

## 실행 예시
```bash
# Ver.A 비주얼 빌드
python scripts/build_deck.py --version A

# Ver.B 텍스트 상세 빌드
python scripts/build_deck.py --version B

# 전체 빌드 + 워터마크
python scripts/build_deck.py --version all --watermark --company "대상사명"
```

## 대상별 커스텀
- `general`: 범용 (기밀정보 제외)
- `[회사명]`: 해당 회사 맞춤 (로고, 워터마크 등)
- `suwon`: 수원시 특화 (지역 경제 파급효과 포함)

## 디자인 도구별 빌드
| 도구 | 명령어 | 출력 |
|------|--------|------|
| python-pptx | `python scripts/build_deck.py` | .pptx |
| Gamma.app | `python scripts/generate_gamma.py` | .pptx/.pdf |
| Pencil | `/pencil-design` 스킬 사용 | .pen |

## 연계 스킬
- `/generate-pptx` — 상세 PPTX 생성 옵션
- `/design-review` — 빌드 후 디자인 검증
- `/pencil-design` — Pencil 에디터로 디자인
