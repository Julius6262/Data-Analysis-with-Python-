#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    
    df_july = df.loc[df["m"] == 7]
    
    mean_july = df_july["Air temperature (degC)"].mean()
    
    return mean_july

def main():
    at = average_temperature()
    print(f"Average temperature in July: {at:.1f}")

if __name__ == "__main__":
    main()
