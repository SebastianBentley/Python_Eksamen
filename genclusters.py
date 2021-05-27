import pandas as pd 
import numpy as np
from sklearn import preprocessing
from sklearn.cluster import estimate_bandwidth
from sklearn.cluster import MeanShift

def create_clusters():
    #Read the csv data
    laptop_data = pd.read_csv('laptops.csv')
    #Apply columns
    laptop_data.columns = ["name", "price"]
    #use label encoder, and change names to numeric values
    label_enc =preprocessing.LabelEncoder()
    laptop_data['name'] = label_enc.fit_transform(laptop_data['name'].astype(str))
    #Estimate the bandwith
    est_bandwidth = estimate_bandwidth(laptop_data)
    #Choose a different bandwith, because it generates more clusters (a lot of laptops are within the same pricerange)
    analyzer = MeanShift(bandwidth=3000)
    #fit the data
    analyzer.fit(laptop_data)
    labels = analyzer.labels_
    #Change the names back to alphabetical value
    laptop_data['name'] = label_enc.inverse_transform(laptop_data['name'])

    #insert the cluster group to each laptop
    laptop_data['cluster_group'] = np.nan
    for i in range(len(laptop_data)):
        laptop_data.iloc[i,laptop_data.columns.get_loc('cluster_group')] = labels[i] #set the cluster label on each row
    #Grouping laptops by Cluster
    laptop_cluster_data = laptop_data.groupby(['cluster_group']).mean()
    #Count of laptops in each cluster
    laptop_cluster_data['Counts'] = pd.Series(laptop_data.groupby(['cluster_group']).size())

    #Save the new dataset with clusters to a file
    laptop_data.to_csv("laptop_csv_data.csv")
    #Save the cluster groups to a file
    laptop_cluster_data.to_csv("clusters.csv")


if __name__ == "__main__":
    create_clusters()
