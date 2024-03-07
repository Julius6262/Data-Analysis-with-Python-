#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    uk_top40_df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    # sum of week on charts by publisher
    best_df = uk_top40_df.groupby("Publisher")["WoC"].sum()
    # Sorted higest sum first
    sorted_best_df = best_df.sort_values(ascending=False)
    # COLUMBIA
    best_publisher = sorted_best_df.index[0]  # Access the first value in the index, that is the one with the higest sum
    #  Selecting the subset where the publisher is COLUMBIA from the orginal dataframe
    subset = uk_top40_df.loc[uk_top40_df["Publisher"]== best_publisher]
    
    return subset
def main():
    best_record_company()
    

if __name__ == "__main__":
    main()
