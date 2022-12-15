from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests


country = "South_Africa"
url = "https://en.wikipedia.org/wiki/"+country

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5'})

url = "https://en.wikipedia.org/wiki/"+country

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
            'Accept-Language':'en-US, en;q=0.5'})
print(flag_link)
rows = soup.find_all("tr")

# capital
capital_c = rows[6].find_all("a")
capital = []
for cap in capital_c:
    title = cap.get('title')
    if title != None:
        capital.append(title)
if len(capital)==1:
    capital = capital[0]

# larget_city
lar_city_c = rows[7].find_all("a")
lar_city = []
for lar_c in lar_city_c:
    lar_city.append(lar_c.get('title'))
if len(lar_city)==1:
    lar_city = lar_city[0]
print(capital)
print(lar_city)

# Language
lang_c = rows[8]
lang = []
if lang_c.find("ul"):
    languages = lang_c.find_all("li")
    for language in languages:
        lang.append(language.find("a").text)
print(lang)