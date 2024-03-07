#!/usr/bin/env python3
import pandas as pd

def main():
    df = pd.read_csv('src/municipal.tsv', sep="\t")
    print(f"Shape: {df.shape[0]}, {df.shape[1]}")  # rows, colums
    columns = df.columns
    
    print("Columns:")
    for i in range(len(columns)):    
        print(columns[i])  


if __name__ == "__main__":
    main()