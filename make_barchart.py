import sys
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    filepath = 'laptops.csv'
    df = pd.read_csv(filepath)
    df.columns = ["name", "price"]
    names = set()
    for value in list(df['name']):
        names.add(value.split(" ")[0])
    
    price_dict = dict()
    for name in names:
        brand_df = df[df['name'].str.contains(name)]
        count = brand_df['name'].count()
        brand_sum = sum(brand_df['price'])
        price_dict[name] = int(brand_sum/count)

    sorted_dict = {k: v for k, v in sorted(price_dict.items(), key=lambda item: item[1])}
    return sorted_dict

def make_bar_chart(sorted_dict):
    plt.bar(sorted_dict.keys(), sorted_dict.values())
    fig1=plt.gcf()
    plt.xticks(rotation=28.5)
    fig1.savefig("barchart.png", dpi=400)
    plt.figure(figsize=(20,10))
    plt.show()

if __name__ == "__main__":
    dict = load_data()
    make_bar_chart(dict)
    #user_input = sys.argv[1:][0]