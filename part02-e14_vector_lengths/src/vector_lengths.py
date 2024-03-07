#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):  # Two dimensional array of shape (n,m) as a parameter
    a_exp =a**2
    a_sum = a_exp.sum(axis=1)
    a_sq = np.sqrt(a_sum)
    return a_sq

def main():
    np.random.seed(9)
    a=np.random.randint(0, 10, (3,2))

    vector_lengths(a)

if __name__ == "__main__":
    main()
