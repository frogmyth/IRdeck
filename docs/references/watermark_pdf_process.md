# 워터마크 PDF 생성 프로세스

## 개요
문서 작성 완료 후, 전달 대상 회사가 정해지면:
1. 회사 로고만 제공 → 반투명 워터마크 자동 생성
2. PPTX 전 슬라이드에 워터마크 자동 삽입
3. PDF 변환
4. 암호 설정 (옵션)

## 프로세스 흐름
```
[회사 로고 PNG] → [워터마크 이미지 자동생성] → [PPTX 워터마크 삽입] → [PDF 변환] → [암호 설정(옵션)]
                    (반투명 + 회전 + 회사명)      (전 슬라이드 배경 레이어)    (PowerPoint/LibreOffice)  (AES-256)
```

## 사용법

### 기본 (워터마크만, 암호 없음)
```bash
python scripts/watermark_pdf.py output/회사소개서/final.pptx --logo assets/icons/aisirius_logo.png
```

### 회사명 포함 + 암호 설정
```bash
python scripts/watermark_pdf.py output/투자제안서/ir_deck.pptx \
  --logo assets/icons/aisirius_logo.png \
  --company "AIsirius Co., Ltd." \
  --password "비밀번호123"
```

### 타일 패턴 (대각선 반복) + 낮은 투명도
```bash
python scripts/watermark_pdf.py output/파트너제안서/tcs_proposal.pptx \
  --logo assets/icons/aisirius_logo.png \
  --style tile \
  --opacity 0.08
```

### 출력 파일 지정
```bash
python scripts/watermark_pdf.py input.pptx --logo logo.png -o "output/최종/신세계_전용.pdf"
```

## 워터마크 스타일 옵션

| 스타일 | 설명 | 추천 용도 |
|--------|------|-----------|
| `center` (기본) | 슬라이드 중앙에 큰 로고 1개 | 일반 배포용 |
| `bottom-right` | 우하단에 작은 로고 | 공식 제출용 (깔끔) |
| `tile` | 대각선 반복 패턴 | 기밀 문서 (복사 방지) |

## 투명도 가이드

| 값 | 효과 | 추천 |
|----|------|------|
| 0.05~0.08 | 거의 안 보임 | 공식 제출용 |
| 0.10~0.15 | 은은하게 보임 | **기본 추천** |
| 0.20~0.30 | 명확하게 보임 | 기밀 문서 |

## PDF 암호 설정 시 보안 수준
- **암호화**: AES-256 (최고 수준)
- **열기 암호**: 지정한 비밀번호
- **텍스트/이미지 추출**: 불가
- **편집/주석**: 불가
- **인쇄**: 저해상도만 허용

## 필요 환경
- Python 3.8+
- `pip install python-pptx Pillow pikepdf`
- PDF 변환: Microsoft PowerPoint (Windows) 또는 LibreOffice

## 대상별 적용 가이드

| 대상 | 워터마크 | 암호 | 스타일 |
|------|---------|------|--------|
| 투자자 (VC/PE) | O | O (필수) | center, opacity 0.12 |
| 파트너사 (TGCS, TCS) | O | 선택 | bottom-right, opacity 0.10 |
| 고객사 (이마트, 롯데) | O | 선택 | center, opacity 0.15 |
| 내부용 | X | X | - |
| 정부 사업 제출 | O | X | bottom-right, opacity 0.08 |
