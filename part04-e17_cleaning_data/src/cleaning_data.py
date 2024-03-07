#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    df = pd.read_csv("src/presidents.tsv", sep="\t")
    df_remove_comma = df.replace(",", "", regex=True)
    
    # Only have numbers in "Start" and remove any month before the year number
    start = df_remove_comma["Start"]
    start_split = start.str.split(" ")
    df_remove_comma["Start"] = start_split.str.get(0)
    
    vp = df_remove_comma["Vice-president"]
    vp_split = vp.str.split(" ")
    # Capitalize the first letter of each word in each sublist
    vp_cap = vp_split.map(lambda sublist: [word.capitalize() for word in sublist])
    # Rearrange the elements if necessary
    vp_rearranged = vp_cap.map(lambda sublist: sublist[::-1] if sublist[0] == "Cheney" or sublist[0] == "Gore" else sublist)
    # Join the words back into a single string for each sublist
    vp_cap_str = vp_rearranged.map(lambda sublist: " ".join(sublist))
    # Assign the corrected strings back to the dataframe
    df_remove_comma["Vice-president"] = vp_cap_str
    

    vp = df_remove_comma["President"]
    vp_split = vp.str.split(" ")
    # Rearrange the elements if necessary
    vp_rearranged = vp_split.map(lambda sublist: sublist[::-1] if sublist[0] == "Bush" or sublist[0] == "Clinton" else sublist)
    # Join the words back into a single string for each sublist
    df_remove_comma["President"]= vp_rearranged.map(lambda sublist: " ".join(sublist))

    # replace "two" with the number 2
    df_remove_comma["Seasons"] = df_remove_comma["Seasons"].replace("two", 2)
    
    #  Convert to float, and if fails replace with NaN
    df_remove_comma["Last"] = df["Last"].replace("-", np.nan)
    


    # Specify the correct data types for each column
    dtypes = {"President": object, "Start": int, "Last": float, "Seasons": int, "Vice-president": object}
    df_remove_comma = df_remove_comma.astype(dtypes)


    return df_remove_comma

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
