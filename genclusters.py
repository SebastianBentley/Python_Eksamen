import pandas as pd 
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import estimate_bandwidth
from sklearn.cluster import MeanShift

def create_clusters():
    laptop_data = pd.read_csv('laptops.csv')
    laptop_data.columns = ["name", "price"]
    label_enc =preprocessing.LabelEncoder()
    laptop_data['name'] = label_enc.fit_transform(laptop_data['name'].astype(str))
    est_bandwidth = estimate_bandwidth(laptop_data)
    analyzer = MeanShift(bandwidth=3000) 
    analyzer.fit(laptop_data)
    labels = analyzer.labels_
    laptop_data['cluster_group'] = np.nan
    for i in range(len(laptop_data)):
        laptop_data.iloc[i,laptop_data.columns.get_loc('cluster_group')] = labels[i] #set the cluster label on each row
    #Grouping laptops by Cluster
    laptop_cluster_data = laptop_data.groupby(['cluster_group']).mean()
    #Count of laptops in each cluster
    laptop_cluster_data['Counts'] = pd.Series(laptop_data.groupby(['cluster_group']).size())
    return laptop_cluster_data


if __name__ == "__main__":
    create_clusters().to_csv("clusters.csv")
