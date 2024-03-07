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

def bicycle_timeseries():
    split_dc_df = split_date_continues()
    date_components = split_dc_df[["Hour","Day", "Month", "Year"]]
    # Make the datetime colum
    split_dc_df["Date"] = pd.to_datetime(date_components)
    # Drop the "old" colums
    split_dc_df.drop(columns=["Year", "Month", "Day", "Hour"], inplace=True)
    split_dc_df.set_index("Date",inplace=True)
    return split_dc_df


def commute():
    bt_df = bicycle_timeseries()
    # Restrict to August 2017
    august_df=bt_df["2017-08-01":"2017-08-31"]
    # Make sure you didn't drop Weekday in the previous function. !!!!!!
    grp_august_df = august_df.groupby("Weekday").sum()
    weekday_mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7
    }
    # Reset the index so that "Weekday" becomes a column again
    grp_august_df.reset_index(inplace=True)

    # Map the weekdays using the mapping dictionary
    grp_august_df["Weekday"] = grp_august_df["Weekday"].map(weekday_mapping)
    grp_august_df.set_index("Weekday", inplace=True)
    return grp_august_df.sort_index()
    
def main():
    commute_df = commute()
    commute_df.plot()
    # Set xticklabels as weekdays automaticly, orderwise:
    # plt.xticks(range(len(commute_df.index)), commute_df.index)
    plt.show()


if __name__ == "__main__":
    main()
