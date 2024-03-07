#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    
    #  Select the specific column, and get the max value
    return df["Snow depth (cm)"].max()

def main():
    max_snow = snow_depth()
    print(f"Max snow depth: {max_snow:.1f}")

if __name__ == "__main__":
    main()
