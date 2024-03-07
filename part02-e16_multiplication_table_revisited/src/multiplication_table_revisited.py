#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    first = np.arange(n)
    second = np.arange(n).reshape(n,1)
    
    return first * second

def main():
    print(multiplication_table(4))

if __name__ == "__main__":
    main()
