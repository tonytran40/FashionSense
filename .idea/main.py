import requests
from bs4 import BeautifulSoup
import re

prices = input("What product do you want to look for? ")
url = f"https://www2.hm.com/en_us/men/products/{prices}.html"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")


print(url)