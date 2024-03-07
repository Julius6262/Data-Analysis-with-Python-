#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    #  -1 to calculate for odd numbers
    y_center = (a.shape[0]-1)/2  # rows
    x_center = (a.shape[1]-1)/2  
    return (y_center, x_center)   # OBS order 

def radial_distance(a):
    h, w = a.shape[0], a.shape[1]
    y, x = center(a)
    Y = np.full((w, h), range(h)).T
    X = np.full((h, w), range(w))
    return np.sqrt((Y-y)**2 + (X-x)**2)

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    #d = a.max()-a.min()
    #return (a - a.min())/d*(tmax - tmin) + tmin
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))

def radial_mask(a):
    return scale(1 - radial_distance(a))

def radial_fade(a):
    return a * radial_mask(a)[:, :, np.newaxis]

def main():
    #a = np.zeros((10, 11, 3))
    a = plt.imread("src/painting.png")
    print(center(a))
    print(radial_distance(a))
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(a)
    ax[1].imshow(radial_mask(a))
    ax[2].imshow(radial_fade(a))
    plt.show()

if __name__ == "__main__":
    main()