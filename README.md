# Job Scraper in Wanted 📰

크롬 브라우저를 활용해 [Wanted](https://www.wanted.co.kr)에서 특정 키워드로 검색된 채용 공고를 자동으로 수집하고, CSV 파일로 저장하는 Python 기반 웹 스크래퍼입니다.

키워드를 수정하여 원하는 분야의 공고를 선택할 수 있습니다.

## 주요 기능
- Playwright를 사용한 브라우저 자동화
- BeautifulSoup를 통한 HTML 파싱
- 키워드별 채용 정보 CSV 저장

## 사용 방법

### 1. 의존성 설치
```bash
pip install python

pip install playwright
pip install beautifulsoup4
```

### 2. 프로젝트 클론
```bash
git clone https://github.com/your-username/wanted-keyword-scraper.git
cd wanted-keyword-scraper
```

### 3. 기술 스택 키워드 변경
```python
keywords = ["flutter", "dart", "unity"] # 다른 기술 스택으로 변경 가능
```
