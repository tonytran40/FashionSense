import requests
from bs4 import BeatifulSoup

def get_price(url):
    r = requests.get(url)
    soup = BeatifulSoup(r.text, 'html.parser')
    price = soup.find('span',{'itemprop':'price'})['cotent']
    return price

print(get_price('https://www.target.com/c/water-bottles-sports-outdoors/-/N-5xt53Zskpj5Z8n35mZ4rii5Zit9rf?type=products&minPrice=1&maxPrice=15'))