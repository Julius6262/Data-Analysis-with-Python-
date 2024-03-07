#!/usr/bin/env python3

import pandas as pd
import numpy as np

def last_week():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')    
    # Since it was last week remove one week from "weeks on chart"
    df['WoC'] -= 1
    
    #  Convert to float, and if fails replace with NaN
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce")
    
    #  Removes the NaN values
    df = df.dropna(subset=["LW"])

    # Check if the current position matches the peak position
    mask1 = df['Peak Pos'] == df['Pos']

    # Check if the current position is less than last week's position
    mask2 = df['Pos'] < df['LW']

    # Set the peak position to NaN for rows where it peaked this week but has dropped in position compared to last week
    df.loc[(mask1 & mask2), 'Peak Pos'] = np.nan
    
    # Sort 
    df = df.sort_values(by=['LW'])
    
    # Set index to the "LW" column
    df.index = df['LW']
    
    # Since we sorted the list we can reindex, and list will have the correct index, and length
    df = df.reindex(range(1,41))
    
    # Give the postion the right value, wich is the same as the index
    df['Pos'] = df.index
    
    # Give NaN value to the last weeks "LW"
    df['LW'] = np.nan
    return df

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
 