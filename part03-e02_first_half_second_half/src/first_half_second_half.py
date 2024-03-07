#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m = a.shape[1]//2  # get number of colums from tuple(row,colum) and calculate m from the formula (n,2*m)
    
    first_half_sum = np.sum(a[:, :m], axis=1)
    last_half_sum = np.sum(a[:, m:], axis=1)

    mask = first_half_sum > last_half_sum
    
    return(a[mask])  # sort the array on the condition

def main():
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2],
              [4, 5, 1, 0]])
    first_half_second_half(a)
if __name__ == "__main__":
    main()
