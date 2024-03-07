#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]  # Remove on index [0], because it is already in the innter nested list
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\s+")
    X1 = df["X1"]
    X2 = df["X2"]
    y = df["y"]

    """# Look at the data in the scatter plot
    plt.scatter(X1, X2)
    plt.show()"""
    """# Test the model with the different values model_0.05, model_0.2, model_0.05
    models = [DBSCAN(eps=v) for v in np.arange(0.05, 0.2, 0.05)]
    
    # To display the different values
    for i, model in enumerate(models, start=1):
        model.fit(df[["X1", "X2"]])  # Fit the model on features X1 and X2
        plt.subplot(2, 2, i)  # Create subplots
        plt.scatter(X1, X2, c=model.labels_, cmap='viridis')
        plt.title(f"DBSCAN with eps={0.05 * i}")
        plt.xlabel("X1")
        plt.ylabel("X2")
    
    plt.tight_layout()
    plt.show()"""
    
    
    esps = np.arange(0.05, 0.2, 0.05)
    results =[]
    for val in esps:
        model = DBSCAN(val)
        model.fit(df[["X1", "X2"]])
        clusters = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        idx = model.labels_ == -1
        outliers = np.count_nonzero(model.labels_ == -1)
        # outliers = np.sum(idx) (both methods of counting outliers and clusters work)
        # clusters = max(model.labels_) + 1
        if clusters == len(y.unique()):
            permutation = find_permutation(clusters, y, model.labels_)
            new_labels = [ permutation[label] for label in model.labels_[~idx]]
            score = accuracy_score(y[~idx], new_labels)
        else: 
            score = np.nan    
        results.append([val, score, clusters, outliers])
    
    return pd.DataFrame(data=results, columns=["eps", "Score", "Clusters", "Outliers"], dtype="float64")
def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
