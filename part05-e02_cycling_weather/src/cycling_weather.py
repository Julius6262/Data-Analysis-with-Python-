import pandas as pd
#!/usr/bin/env python3


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


def cycling_weather():
    cycling_data = split_date_continues()
    weather_data = pd.read_csv('src/kumpula-weather-2017.csv', sep=',')
    merged_df = pd.merge(cycling_data, weather_data, left_on=['Year', 'Month', 'Day'], right_on=['Year', 'm', 'd'])
    
    #  Drop for colums and dropna for rows
    new_df = merged_df.drop(columns=['m', 'd', 'Time', 'Time zone'])
    
    
    
    return new_df

def main():
    cycling_weather()
    import numpy as np
    def sum_strings(x, y):
        x = np.array(list(x),dtype=int)
        y = np.array(list(y),dtype=int)
    
        result_arr = x + y

        return "".join(map(str,result_arr))


    
    print(sum_strings("123", "456"))


if __name__ == "__main__":
    main()
