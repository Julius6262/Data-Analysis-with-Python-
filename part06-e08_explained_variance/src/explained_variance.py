#!/usr/bin/env python3
from math import exp
from numpy.core.fromnumeric import cumsum
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    # Read the data from the tsv file into a DataFrame
    df = pd.read_csv("src/data.tsv", sep="\s+")
    
    # Calculate the variance along each column (feature) of the DataFrame
    v = df.var(axis=0)
    
    # Initialize a PCA (Principal Component Analysis) object
    pca = PCA()
    
    # Fit the PCA model to the data
    pca.fit(df)
    
    # Get the explained variances from the fitted PCA model
    ev = pca.explained_variance_
    
    # Return both the variances and explained variances
    return v, ev
    

def main():
    # Call the function to get variances and explained variances
    v, ev = explained_variance()
    
    # Print the variances in the right format
    print("The variances are:", end=" ")
    for v in v.values:
        print(f"{v:.3f}", end=" ")
    print()
    
    # Print the explained variances after PCA in the right format
    print("The explained variances after PCA are:", end=" ")
    for v in ev:
        print(f"{v:.3f}", end=" ")
    
    # Calculate the cumulative sum of explained variances
    cum_sum = np.cumsum(ev)
    
    # Get the number of terms (components) in the PCA
    num_terms = len(cum_sum)
    
    # Plot the cumulative explained variance against the number of components
    plt.plot(np.arange(1, 1+num_terms), cum_sum)
    plt.show()
if __name__ == "__main__":
    main()
