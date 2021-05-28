import bs4
import requests
import sys
import re
import csv
import platform


def get_laptops(page_number:int):
    url = "https://www.proshop.dk/Baerbar?pn="+str(page_number)
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

    return sorted_laptops

def generate_csv(output_file, dic):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None
    with open(output_file, 'a', newline=newline) as f:
        for value in dic.keys():
            f.write(value + ",")
            f.write(dic[value] + "\n")

           
if __name__ == "__main__":
    file = "laptops.csv"
    for x in range(1, 54):
        #generate_csv(file, get_laptops(x))