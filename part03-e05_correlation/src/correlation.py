#!/usr/bin/env python3

import scipy.stats as ss
import numpy as np
import pandas as pd

def load():
    #  Return (sepal length (cm), sepal width (cm), petal length (cm), petal width (cm))
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    full_data = load()
    sepal_length = full_data[:, 0]
    petal_length = full_data[:, 2]
    
    # Calculate Pearson correlation coefficient and p-value
    correlation_coefficient, p_value = ss.pearsonr(sepal_length, petal_length)
    

    return correlation_coefficient

def correlations():
    full_data = load()
    #  returns an array of shape (n, n), where n is the number of variables (columns) in the dataset
    correlation_matrix = np.corrcoef(full_data, rowvar=False)  # rowvar = False for colum instead of rows. each coloum represents a length or width
    
    return correlation_matrix

def main():
    print(load())
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
