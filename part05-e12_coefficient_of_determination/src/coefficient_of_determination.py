#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")
    model = LinearRegression(fit_intercept=True)
    Y = df["Y"]
    # Get x colums 
    X = df.loc[:, "X1": "X5"]
    model.fit(X, Y)
    r2_score = model.score(X,Y)
    r2_list = [r2_score]
    
    for column in df.columns:  # Iterate through all columns
        r = df.loc[:, column]  # acess all rows in the colum
        r = r.values.reshape(-1,1)  #  converting the 1D array of values in r into a 2D array with a single column.
        model.fit(r,Y)
        s = model.score(r, Y)
        r2_list.append(s)

    return r2_list # list containing only the R2-score
    
    
def main():
    r2 = coefficient_of_determination()
    for i in range(0,(len(r2)-1)):
        if i == 0:
            print(f"R2-score with feature(s) X: {r2[i]}")
        else:
            print(f"R2-score with feature(s) X{i}: {r2[i]}")
if __name__ == "__main__":
    main()
