#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from scipy.spatial.kdtree import distance_matrix
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]  # Remove on index [0], because it is already in the innter nested list
        permutation.append(new_label)
    return permutation

def toint(x):
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return mapping.get(x, 10)

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\s+')
    feature_matrix = [[toint(c) for c in s] for s in df["X"]]
    
    y = df["y"]
    y = y.to_numpy()
    label_vector = y
    
    return np.array(feature_matrix), label_vector

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    # The feature matrix is typically denoted as X, and the corresponding label vector is denoted as y.
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average')
    model.fit(X)
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [ permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    return score
    


def cluster_hamming(filename):
    # Extract features and labels
    X, y = get_features_and_labels(filename)
    
    # Compute Hamming distance matrix
    hamming_distances = pairwise_distances(X, metric='hamming')
    
    # Create AgglomerativeClustering model
    model = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
    
    # Fit the model with Hamming distance matrix
    model.fit_predict(hamming_distances)
    
    # Step 5: Calculate accuracy score
    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    score = accuracy_score(y, new_labels)
    
    return score

    
def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
