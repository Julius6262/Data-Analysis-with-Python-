#!/usr/bin/env python3
import pandas as pd

def subsetting_with_loc():
    # Read the dataset
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    
    # Subset the DataFrame using loc to select rows from Akaa to Äänekoski
    # and columns: "Population", "Share of Swedish-speakers of the population, %", and "Share of foreign citizens of the population, %"
    subset_df = df.loc["Akaa":"Äänekoski", ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    
    return subset_df

def main():
    subsetting_with_loc()

if __name__ == "__main__":
    main()
