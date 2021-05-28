import pandas as pd


def get_close_five(name, price):
    #filepaths
    filepath = 'laptop_cluster_data.csv'
    filepath2 = 'clusters.csv'
    #load the csv files
    laptops = pd.read_csv(filepath)
    clusters = pd.read_csv(filepath2)

    #find the specific cluster to the laptop
    cluster_price = min(list(clusters['price']), key=lambda x:abs(x-price))
    found_cluster = clusters.loc[clusters['price'] == cluster_price]['cluster_group']

    #Find the laptops in the same cluster
    same_cluster = laptops.loc[laptops['cluster_group'] == float(found_cluster)][['name','price']]
    #Find different laptops, than the one being searched
    final_laptops = same_cluster.loc[same_cluster['name'] != name][['name', 'price']]
    
    #Get the final close-priced laptops
    results = final_laptops.iloc[(same_cluster['price']-price).abs().argsort()[:5]]
    return results

if __name__ == "__main__":
    print(get_close_five("lenovo blade 13", 14560))






