#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    # Read the CSV file into a DataFrame
    df = pd.read_csv("src/who_suicide_statistics.csv")
    
    # Drop unnecessary columns ('year', 'sex', 'age')
    df = df.drop(columns=['year', 'sex', 'age'])
    
    # Calculate the suicide fractions
    df['suicide_fraction'] = df['suicides_no'] / df['population']
    # calculate the maean and group by country
    mean_suicide_fractions = df.groupby('country')['suicide_fraction'].mean()
    
    return mean_suicide_fractions

def main():
    suicide_fractions()

if __name__ == "__main__":
    main()
