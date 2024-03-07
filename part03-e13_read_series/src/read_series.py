#!/usr/bin/env python3
import pandas as pd

def read_series():
    index_list = []
    value_list = []
    while True:
        user_input = input("type lines: ")
        if not user_input:
            break
            
        try:
            index, value = user_input.split()
            index_list.append(index)
            value_list.append(value)
        
        except:
            print("invalid input")
    
    
    series = pd.Series(value_list, index = index_list)
    return series

def main():
    read_series()

if __name__ == "__main__":
    main()
