from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

class KeywordScraper:
    def __init__(self, keywords):
        self.keywords = keywords
        self.result = {}

    def scrap(self, akeyword, page):
        page.goto(f"https://www.wanted.co.kr/search?query={akeyword}&tab=position")

        for i in range(5):
            page.keyboard.down("End")
            time.sleep(3)


        content = page.content()

        time.sleep(3)

        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__zQcZs JobCard_container--variant-card___dlv1")

        jobs_db = []

        for job in jobs:
            company_name = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__company__ByVLu wds-nkj4w6").text
            career_time = job.find("span", class_="CompanyNameWithLocationPeriod_CompanyNameWithLocationPeriod__location__4_w0l wds-nkj4w6").text
            link = f"https://wanted.co.kr{job.find('a')['href']}"

            job_dict = {
                "company_name": company_name,
                "career_time": career_time,
                "link": link
            }

            jobs_db.append(job_dict)
        
        return jobs_db


    def save_to_csv(self, akeyword, jobs_db):
        file = open(f"{akeyword}.csv", "w", encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(["company_name", "career_time", "link"])

        for job in jobs_db:
            writer.writerow(job.values())

        file.close()

    def run(self):
        p = sync_playwright().start()

        browser = p.chromium.launch(headless=False) # keyword arguments

        # def plus(a,b): # positional arguments
        #     return a+b

        page = browser.new_page()

        for k in self.keywords:
            self.save_to_csv(k,self.scrap(k, page))
        
        p.stop()


keywords = ["flutter", "dart", "unity"]
k = KeywordScraper(keywords)
k.run()
