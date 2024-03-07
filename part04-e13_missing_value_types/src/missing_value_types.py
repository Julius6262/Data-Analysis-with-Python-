#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    state = ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]
    y_independence = [np.nan,1917,1776,1523,np.nan,1992]
    president = [np.nan, "Niinistö", "Trump", np.nan, "Steinmeier", "Putin"]
    
    data = {"State": state, "Year of independence": y_independence, "President": president}
    
    df = pd.DataFrame(data)
    
    df = df.set_index("State")  # Set the "State" column as the index

    return df

# Could also have been done this way
"""df=pd.DataFrame([["United Kingdom", np.nan, None],
                     ["Finland",        1917,   "Niinistö"],
                     ["USA",            1776,   "Trump"],
                     ["Sweden",         1523,   None],
                     ["Germany",        np.nan, "Steinmeier"],
                     ["Russia",         1992,   "Putin"]],
                    columns=["State", "Year of independence", "President"])
    df = df.set_index("State")"""
               
def main():
    missing_value_types()

if __name__ == "__main__":
    main()
