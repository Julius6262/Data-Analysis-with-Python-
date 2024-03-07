#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    a = df["Päivämäärä"]
    b = a.str.split(expand=True)
    b.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    weekdays = {
        'ma': 'Mon',
        'ti': 'Tue',
        'ke': 'Wed',
        'to': 'Thu',
        'pe': 'Fri',
        'la': 'Sat',
        'su': 'Sun'
    }
    months = {
        'tammi': 1,
        'helmi': 2,
        'maalis': 3,
        'huhti': 4,
        'touko': 5,
        'kesä': 6,
        'heinä': 7,
        'elo': 8,
        'syys': 9,
        'loka': 10,
        'marras': 11,
        'joulu': 12
    }
    c = b['Weekday']
    d = c.map(weekdays)
    b['Weekday'] = d
    e = b['Month']
    f = e.map(months)
    f = f.map(int)
    b['Month'] = f
    g = b['Hour']
    h = g.map(lambda x: x[:2])
    h = h.map(int)
    b['Hour'] = h
    i = b['Day']
    i = i.map(int)
    b['Day'] = i
    j = b['Year']
    j = j.map(int)
    b['Year'] = j
    return (b, df)

def split_date_continues():
    # Call the split_date() function to extract the date components and the original DataFrame
    dates, df = split_date()
    
    # Remove rows containing all missing values from the DataFrame
    df.dropna(how='all', inplace=True)
    
    # Remove columns containing all missing values from the DataFrame
    df.dropna(axis=1, how='all', inplace=True)
    
    # Drop the 'Päivämäärä' column as it has been split into separate date components
    df.drop(["Päivämäärä"], axis=1, inplace=True)
    
    # Concatenate the date components DataFrame 'dates' with the modified DataFrame 'df' along columns
    final = pd.concat([dates, df], axis=1)
    
    # Return the final DataFrame containing both the date components and the modified original DataFrame
    return final

def cyclists_per_day():
    cycling_df = split_date_continues()
    cycling_df.drop(["Hour","Weekday"], axis=1, inplace=True)
    groups = cycling_df.groupby(["Year", "Month", "Day"]).sum()
    
    return groups
    
def main():
    # Get daily counts using cyclists_per_day function
    daily_counts = cyclists_per_day()

    # Restrict data to August 2017
    august_2017 = daily_counts.loc[(2017, 8):]

    august_2017.plot()
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
