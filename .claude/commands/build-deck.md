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
4. python-pptx 스크립트 실행 (`scripts/`)
5. 출력 (`output/`)

## 대상별 커스텀
- `general`: 범용 (기밀정보 제외)
- `[회사명]`: 해당 회사 맞춤 (로고, 워터마크 등)
- `suwon`: 수원시 특화 (지역 경제 파급효과 포함)
