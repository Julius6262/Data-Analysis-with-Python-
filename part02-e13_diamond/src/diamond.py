#!/usr/bin/env python3

import numpy as np

def diamond(n):
    if n == 1:
        return np.array([[1]], dtype=int)
    diamond_center = np.eye(n, dtype = int)
    #print(diamond_center)

    left_side = diamond_center[:, ::-1]  # Create the left side of the diamond by reversing the columns of the central part
    
    right_side = diamond_center[:, 1:]
    
    diamond_upper = np.concatenate((left_side,right_side), axis=1)

    diamond_lower = diamond_upper[::-1]
    diamond_lower = diamond_lower[1:]  # Remove the top, to avoid duplication in the middel of the diamond

    full_diamond = np.concatenate((diamond_upper,diamond_lower), axis=0)
    return full_diamond

def main():
    diamond(3)

if __name__ == "__main__":
    main()
