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
    href = soup.select('a[class="product-link"]')
    laptops = {}
    new_href = list()

    for idx, val in enumerate(href):
        if((idx%2)==0):
            new_href.append(href[idx])


    for idx, val in enumerate(names):
        if('baerbar' in str(new_href[idx])):
            laptops[names[idx].getText()] = prices[idx].getText()

    regex_prices = re.compile(r'([\w.]+)')
    for name in laptops.keys():
        format_price = (regex_prices.findall(laptops.get(name))[0]).replace('.','')
        laptops[name] = format_price

    sorted_laptops = {k: v for k, v in sorted(laptops.items(), key=lambda item: item[1])}
    
    #Fejlhåndtering hvis laptop ikke findes
    if not list(sorted_laptops.items()):
        return {"Ikke fundet": ("Ikke fundet","0")}
    
    #Laptop fundet
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
    
    #Fejlhåndtering hvis laptop ikke findes
    if not list(sorted_laptops.items()):
        return {"Ikke fundet": ("Ikke fundet","0")}
    
    #Laptop fundet
    result = list(sorted_laptops.items())[0]
    return {"Proshop.dk":result}

def elgiganten(user_input):
    url = "https://www.elgiganten.dk/search?SearchTerm=" + user_input
    r = requests.get(url)
    r.raise_for_status()
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    names = soup.select('span[class="table-cell"]')
    prices = soup.select('div[class="product-price"]')
    href = soup.select('a[class="product-name"]')
    laptops = {}
    regex_prices = re.compile(r'([0-9]+)')

    for idx, val in enumerate(names):
        if ((prices[idx].get_text() != '\n\xa0\n\xa0\n') and str(href[idx]).find('barbar') != -1):
            price = prices[idx].get_text(strip=True).replace('\xa0', '')
            laptops[names[idx].get_text()] = regex_prices.findall(price)[0]

    sorted_laptops = {k: v for k, v in sorted(laptops.items(), key=lambda item: item[1])}

    #Fejlhåndtering hvis laptop ikke findes
    if not list(sorted_laptops.items()):
        return {"Ikke fundet": ("Ikke fundet","0")}

    #Laptop fundet
    result = list(sorted_laptops.items())[0]
    return {"Elgiganten.dk":result}



def fetch_data(user_input: str):
    final_input = user_input.replace(' ', '+')
    komplettdata = (komplett(final_input))
    #proshopdata = (proshop(final_input))
    elgigantendata = (elgiganten(final_input))
    cheapest = find_cheapest([komplettdata, elgigantendata])
    return cheapest

def find_cheapest(laptop_data: list):
    minimum = int(list(laptop_data[0].values())[0][1])
    result = list(laptop_data[0].items())[0]
    for idx, val in enumerate(laptop_data):
        value = int(list(val.values())[0][1])
        if ( value < minimum and value != 0 ):
            result = list(val.items())[0]
    return result


if __name__ == "__main__":
    user_input = sys.argv[1:][0]