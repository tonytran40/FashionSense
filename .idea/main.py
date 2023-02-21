import requests
from bs4 import BeautifulSoup
import re

products = input("What product do you want to look for? ")
url = f"https://www.uniqlo.com/us/en/search?q={products}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text=doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][-1])

for page in range(1,pages+1):
    url = f"https://www.uniqlo.com/us/en/search?q={products}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="fr-ec-product-collection fr-ec-product-collection--type-grid")
    
    items = div.find_all(text=re.compile(products))
    for item in items:
        print(item)
    