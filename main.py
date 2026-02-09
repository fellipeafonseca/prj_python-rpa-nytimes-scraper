import pandas as pd
import logging
import re
from datetime import datetime
from urllib.parse import urlencode
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ================= CONFIG ================= #

class ConfigManager:
    def __init__(self, config_path="config.json"):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        import json
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def get(self, key):
        return self.config.get(key)


# ================= SCRAPER ================= #

class NYTimesScraper:
    def __init__(self, config: ConfigManager):
        self.config = config

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
      #  options.add_argument("--start-maximized")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        
       
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        

       


    def search_news(self):
        logging.info("Iniciando busca de notícias...")
        news_list = []

        regex_money = r"(?:US\$|\$)\s?\d+"
        regex_date = r"\b\d{4}[-/]\d{2}[-/]\d{2}\b"

        meses = self.config.get("meses")
        start_date = datetime.now() - relativedelta(months=meses)
        start_date = datetime(start_date.year, start_date.month, 1).strftime("%Y-%m-%d")
        end_date = datetime.now().strftime("%Y-%m-%d")

        params = {
            "query": self.config.get("frase"),
            "startDate": start_date,
            "endDate": end_date,
            "lang": self.config.get("idioma"),
            "types": self.config.get("tipo"),
            "sort": self.config.get("ordenacao"),
        }

        url = f"{self.config.get('url')}?{urlencode(params)}"
        logging.info(f"URL de busca: {url}")

        try:

            self.driver.get(url)

            self._handle_cookies()
            self._expand_results()

            articles = self.driver.find_elements(By.XPATH, "//ol[@data-testid='search-results']/li[@class='kyt-wCDWp']")
            logging.info(f"Notícias Encontradas: {len(articles)}")

            for article in articles:
                title = article.find_element(By.CSS_SELECTOR, "h4").text
                link = article.find_element(By.TAG_NAME, "a").get_attribute("href")

                description = (
                    article.find_element(By.CLASS_NAME, "css-e5tzus").text
                    if article.find_elements(By.CLASS_NAME, "css-e5tzus")
                    else ""
                )

                image = (
                    article.find_element(By.TAG_NAME, "img").get_attribute("src")
                    if article.find_elements(By.TAG_NAME, "img")
                    else ""
                )

                date_match = re.search(regex_date, link)
                date = date_match.group(0) if date_match else ""

                has_money = bool(re.search(regex_money, title + description))
                ocorrencias = (title + description).lower().count(
                    self.config.get("frase").lower()
                )

                news_list.append({
                    "Título": title,
                    "Data": date,
                    "Descrição": description,
                    "Imagem": image,
                    "Número de Ocorrências": ocorrencias,
                    "Valor Monetário": has_money
                })

        finally:
             self.driver.quit()

        return news_list

    def _handle_cookies(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/button[2]"))
            ).click()
        except:
            pass
  

    def _expand_results(self):
        while True:
            try:
                self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Show More']"))
                ).click()
            except:
                break


# ================= STORAGE ================= #

class DataStorage:
    @staticmethod
    def save_to_excel(data, filename="noticias.csv"):
        logging.info(f"{len(data)} Salvando dados em arquivo...")
        pd.DataFrame(data).to_csv(filename, index=False)


# ================= BOT ================= #

class NYTimesBot:
    def __init__(self):
        self.config = ConfigManager()
        self.scraper = NYTimesScraper(self.config)

    def run(self):
        data = self.scraper.search_news()
        DataStorage.save_to_excel(data)
        logging.info("Processo finalizado com sucesso!")


if __name__ == "__main__":
    NYTimesBot().run()
