#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    
     # Remove empty rows at the end
    df = df.dropna(how='all')

    # Remove columns that contain only missing values
    df = df.dropna(axis=1, how='all')

    pai_df = df["Päivämäärä"]
    b = pai_df.str.split(expand=True)
    
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
    # Give the weekdays new names
    b['Weekday'] = b['Weekday'].map(weekdays)
    

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
    
    f = b['Month'].map(months)
    f = f.map(int)
    b['Month'] = f
    
    # sort out the .00 after the minut clock
    h = b['Hour'].map(lambda x: x[:2])
    h = h.map(int)
    b['Hour'] = h
    
    i = b['Day'].map(int)
    b['Day'] = i
    
    j = b['Year'].map(int)
    b['Year'] = j
    
    
    return b

def main():
    split_date()
       
if __name__ == "__main__":
    main()
