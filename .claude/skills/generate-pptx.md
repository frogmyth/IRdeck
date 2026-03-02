# PPTX 생성 스킬

python-pptx를 사용하여 투자제안서/회사소개서 PPTX를 자동 생성합니다.

## 사용법
`/generate-pptx [유형] [대상]`
- 유형: ir-deck | company-intro | partner-proposal | cms-intro
- 대상: general | [회사명] (예: tcs, nri, 신세계)

## 동작
1. `docs/content/` 디렉토리에서 해당 유형의 콘텐츠 원고 로드
2. `templates/` 디렉토리에서 PPTX 템플릿 로드
3. `assets/` 디렉토리에서 이미지/인포그래픽 매핑
4. python-pptx로 슬라이드 생성:
   - 텍스트 배치 (폰트, 크기, 색상, 정렬)
   - 이미지 삽입 (위치, 크기)
   - 인포그래픽: 배경 이미지 + 텍스트 레이어 분리 오버레이
5. 대상별 커스텀 처리:
   - 회사명/로고 삽입
   - 기밀 정보 필터링
   - 워터마크 적용 (필요시)
6. `output/[유형]/` 디렉토리에 저장

## 이미지 처리 규칙
- 인포그래픽 텍스트 → python-pptx 텍스트 박스로 오버레이 (수정 가능)
- 원근감 적용 텍스트 → 이미지 내 포함 (나노바나나2로 생성)
- 차트/도표 → python-pptx 차트 객체 또는 이미지

## 출력
- `output/[유형]/AIsirius_[유형]_[대상]_[날짜].pptx`
