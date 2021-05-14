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
    result = list(sorted_laptops.items())[0]
    return {"Komplett.dk":result}

def proshop(user_input):
    url = "https://www.proshop.dk/?pre=0&s=" + user_input + "&c=baerbar"
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    names = soup.select('a[class="site-product-link"] > h2')
    prices = soup.select('span[class="site-currency-lg"]')
    laptops = {}

    for idx, val in enumerate(names):
        laptops[names[idx].getText()] = prices[idx].getText()

    regex_prices = re.compile(r'([\w.]+)')
    for name in laptops.keys():
        format_price = (regex_prices.findall(laptops.get(name))[0]).replace('.','')
        laptops[name] = format_price

    sorted_laptops = {k: v for k, v in sorted(laptops.items(), key=lambda item: item[1])}
    result = list(sorted_laptops.items())[0]
    return {"Proshop.dk":result}

def elgiganten(user_input):
    url = "https://www.elgiganten.dk/search?SearchTerm=" + user_input
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    names = soup.select('span[class="table-cell"]')
    prices = soup.select('div[class="product-price"]')
    laptops = {}
    regex_prices = re.compile(r'([0-9]+)')
    
    for idx, val in enumerate(names):
        if not((prices[idx].get_text() == '\n\xa0\n\xa0\n')):
            price = prices[idx].get_text(strip=True).replace('\xa0', '')
            laptops[names[idx].get_text()] = regex_prices.findall(price)[0]


    sorted_laptops = {k: v for k, v in sorted(laptops.items(), key=lambda item: item[1])}
    result = list(sorted_laptops.items())[0]
    return {"Elgiganten.dk":result}



def fetch_data(user_input: str):
    final_input = user_input.replace(' ', '+')
    komplettdata = (komplett(final_input))
    proshopdata = (proshop(final_input))
    elgigantendata = (elgiganten(final_input))

    return [komplettdata, proshopdata, elgigantendata]

def find_cheapest(laptop_data: list):
    minimum = int(list(laptop_data[0].values())[0][1])
    for idx, val in enumerate(laptop_data):
        if ( int(list(val.values())[0][1]) < minimum):
            minimum = int(list(val.values())[0][1])
    return minimum


if __name__ == "__main__":
    user_input = sys.argv[1:][0]
    laptop_data = fetch_data(user_input)
    find_cheapest(laptop_data)