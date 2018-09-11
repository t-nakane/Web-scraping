# Web scraping
# https://www.sejuku.net/blog/51241

import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = requests.get(self.site)
        parser = "html.parser"
        sp = BeautifulSoup(r.content, parser)
        for i in sp.select("p.ttl"):
            print(i.getText())

news = "https://news.yahoo.co.jp/"
Scraper(news).scrape()
