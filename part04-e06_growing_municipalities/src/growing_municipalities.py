#!/usr/bin/env python3
import pandas as pd

def growing_municipalities(df):
    
    #get the length of the total number of municipalities, from the right colum
    num_municipalities = len(df["Population change from the previous year, %"])
    
    #get the length of municipalities with growing population using boolean mask
    newer_df = df.loc[df["Population change from the previous year, %"] > 0]
    
    num_growing_population = len(newer_df)
    
    dec = (num_growing_population/num_municipalities)
    
    return dec

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    df_municipalities = df["Akaa":"Äänekoski"]
    dec = growing_municipalities(df_municipalities)
    print(f"Proportion of growing municipalities: {dec:.1f}%")


if __name__ == "__main__":
    main()