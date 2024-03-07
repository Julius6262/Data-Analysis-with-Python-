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
    
def suicide_weather():
    suicide_df = suicide_fractions()
    df_avg_weather = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col="Country")[0    ]
    df = df_avg_weather.sort_index(ascending=True)
    
    # Replace unicode minus sign with regular minus sign
    df['Average yearly temperature (1961–1990, degrees Celsius)'] = df['Average yearly temperature (1961–1990, degrees Celsius)'].str.replace("\u2212", "-")

    # Convert temperature column to float
    df['Average yearly temperature (1961–1990, degrees Celsius)'] = df['Average yearly temperature (1961–1990, degrees Celsius)'].astype(float)
    # Calculate the Spearman correlation
    new_df = pd.merge(df, suicide_df, left_index=True, right_index=True)
    correlation = new_df.corr(method='spearman').iloc[0, 1]
    (suicide_rows, temperature_rows, common_rows) = (x.shape[0] for x in [suicide_df, df, new_df])
    return suicide_rows, temperature_rows, common_rows, correlation

def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")

if __name__ == "__main__":
    main()
