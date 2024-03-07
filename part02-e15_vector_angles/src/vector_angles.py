#!/usr/bin/env python3

import numpy as np


import numpy as np

def vector_angles(X, Y):
    inner_products = np.sum(X * Y, axis=1)
    vector_lengths = np.sqrt(np.sum(X ** 2, axis=1)) * np.sqrt(np.sum(Y ** 2, axis=1))
    angles_radians = np.arccos(np.clip(inner_products / vector_lengths, -1.0, 1.0))
    angles_degrees = angles_radians * (180 / np.pi)
    return angles_degrees


def main():
    np.random.seed(9)
    X= np.random.randint(0, 10, (3,2))
    Y = np.random.randint(0, 10, (3,2))
    vector_angles(X,Y)

if __name__ == "__main__":
    main()
