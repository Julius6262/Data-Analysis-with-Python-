#!/usr/bin/env python3

import scipy
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]  # Remove on index [0], because it is already in the innter nested list
        permutation.append(new_label)
    return permutation

def plant_clustering():
    data = load_iris()
    # Check the keys and look at their data
    """print(data.keys())
    print(data.data[:10])
    print(data.target[:10])"""
    
    X, y = data.data, data.target
    """# Look at the data in a scatter plot. 
    print(X.shape)  # 4 columns
    # You can change the two numbers from 0-3, to look at the different data
    plt.scatter(X[:,0],X[:,1])
    plt.show()"""

    km_model = KMeans(n_clusters = 3, random_state=0)
    km_model.fit(X)
    # print(km_model.cluster_centers_)  # You can display the Cluster centers
    
    """# Look at the data with the cluster centers again 
    # You can change the two numbers from 0-3, to look at the different data
    
    plt.scatter(X[:,0],X[:,1], c=km_model.labels_)  # each cluster will have different colors
    # Select the cluster centers first and second coordinates, set the size to 100. 
    plt.scatter(km_model.cluster_centers_[:,0], km_model.cluster_centers_[:,1], s=100, color="red") # Show the centres
    plt.show()
    """
    
    permutation = find_permutation(3, y, km_model.labels_)
    new_labels = [ permutation[label] for label in km_model.labels_]   # permute the labels
    permutation_acc = accuracy_score(y, new_labels) # 0.887
    
    acc_no_permutation = accuracy_score(y, km_model.labels_)  # 0.24

    return permutation_acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
