#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    inverse_s = pd.Series(s.index, index=s.values)
    return inverse_s

def main():
    s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
    inverse_s = inverse_series(s)
    print(inverse_s)

if __name__ == "__main__":
    main()
