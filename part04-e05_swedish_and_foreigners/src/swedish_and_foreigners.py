#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    # Read the municipalities data set from the specified file, using a tab as the separator and setting 'Region 2018' column as the index
    df = pd.read_csv('src/municipal.tsv', sep="\t", index_col="Region 2018")
    
    # Select a subset of municipalities from 'Akaa' to 'Äänekoski'
    municipalities = df["Akaa":"Äänekoski"]
    
    # Create boolean conditions to identify municipalities where the proportion of Swedish speakers and foreigners both exceed 5%
    swedish_speakers_condition = df["Share of Swedish-speakers of the population, %"] > 5
    foreign_citizens_condition = df["Share of foreign citizens of the population, %"] > 5
    
    # Combine the conditions using bitwise AND (&) to get municipalities where both conditions are true
    swedish_speakers_and_foreigners = swedish_speakers_condition & foreign_citizens_condition 
    
    # Filter the municipalities DataFrame to include only those where both conditions are true
    df_sf = municipalities[swedish_speakers_and_foreigners]
    
    # Select specific columns from the filtered DataFrame to display
    df_show = df_sf.loc[:, ["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]
    
    
    return df_show

def main():
    # Print the DataFrame returned by the swedish_and_foreigners function
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
