# web scraping Nikkei

import requests
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

title = soup.title.string

print(title)
