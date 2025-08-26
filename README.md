# Job Scraper in Wanted 📰

This Python-based web scraper automatically collects job postings searched for with specific keywords on [Wanted](https://www.wanted.co.kr) using the Chrome browser and saves them as a CSV file.

You can edit keywords to select postings in your desired field.

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
