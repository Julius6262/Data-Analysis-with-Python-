#!/usr/bin/env python3
import numpy as np
import pandas as pd

def top_bands():
    bands_df = pd.read_csv('src/bands.tsv', sep='\t')
    uk_top40_df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    #  Change the formatting of the strings to the same format title. 
    bands_df['Band'] = bands_df['Band'].str.title()
    uk_top40_df['Artist'] = uk_top40_df['Artist'].str.title()
    
    # Perform the merge based on the 'Artist' column in uk_top40_df and the 'Band' column in bands_df
    merged_df = pd.merge(uk_top40_df, bands_df, left_on=['Artist'], right_on=['Band'])

    return merged_df

def main():
    top_bands()
    return

if __name__ == "__main__":
    main()
