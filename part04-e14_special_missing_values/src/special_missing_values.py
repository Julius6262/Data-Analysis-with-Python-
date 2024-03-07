#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    
    
    # Convert "Pos" and "LW" columns to numeric, if it fails fx with "New" or "Re", makes it NaN
    df["Pos"] = pd.to_numeric(df["Pos"], errors="coerce")
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce")
    
    # Boolean indexing
    show_df = df[df["Pos"] > df["LW"]]
    return show_df
def main():
    special_missing_values()

if __name__ == "__main__":
    main()
