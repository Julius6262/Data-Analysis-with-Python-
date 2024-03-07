#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    # Accessing the values in each row
    second_firs_colum = a[:, 1]
    second_last_colum = a[:, -2]

    # Making the comparing
    c = second_firs_colum > second_last_colum
    
    # Maskig. returning the values of the parameter metrix, that are true to the conditon
    return a[c]
    
def main():
    a = np.array([[8, 9, 3, 8, 8],
                [0, 5, 3, 9, 9],
                [5, 7, 6, 0, 4],
                [7, 8, 1, 6, 2],
                [2, 1, 3, 5, 8]])

    column_comparison(a)
    

if __name__ == "__main__":
    main()
