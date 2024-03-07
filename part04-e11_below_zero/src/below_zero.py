#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    
    under_0 = df.loc[df["Air temperature (degC)"] < 0]
    
    #  Count rows using shape that returns [rows, colums]
    count_under_0 = under_0.shape[0]
    
    return count_under_0

def main():
    bz = below_zero()
    print(f"Number of days below zero: {bz}")
    
if __name__ == "__main__":
    main()
