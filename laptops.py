import bs4
import requests
import sys
import re

def komplett(user_input):
    url = "https://www.komplett.dk/search?q=" + user_input
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    names = soup.select('div[class="text-content"] > h2')
    prices = soup.select('span[class="product-price-now"]')

    laptops = {}

    for idx, val in enumerate(names):
        laptops[names[idx].getText()] = prices[idx].getText()

    regex_prices = re.compile(r'([\w.]+)')
    for name in laptops.keys():
        format_price = (regex_prices.findall(laptops.get(name))[0]).replace('.','')
        laptops[name] = format_price

    sorted_laptops = {k: v for k, v in sorted(laptops.items(), key=lambda item: item[1])}
    
    return sorted_laptops



def start(user_input: str):
    final_input = user_input.replace(' ', '+')
    #komplett(final_input)
    print(komplett(final_input))


if __name__ == "__main__":
    user_input = sys.argv[1:][0]
    start(user_input)