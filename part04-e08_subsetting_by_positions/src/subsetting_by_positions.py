#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    
    #  Boolean mask
    df_top_10 = df[df["Pos"] <= 10]

    # Show colums that is true to the mask
    df_show = df_top_10[["Title", "Artist"]]
    return df_show  # Alternative solution "df.iloc[:10,2:4]"

def main():
    subsetting_by_positions()

if __name__ == "__main__":
    main()
