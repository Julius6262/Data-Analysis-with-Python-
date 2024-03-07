#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(arr):
    fig, ax = plt.subplots(1, 2)  # Create a figure with 1 row and 2 columns for subplots
    
    x1 = arr[:, 0]
    y1 = arr[:, 1]
    
    color = arr[:, 2]  # Extract color values from the third column
    size = arr[:, 3]   # Extract size values from the fourth column
    
    ax[0].plot(x1, y1)  # Plot data on the first subplot
    ax[1].scatter(x1,y1, c=color, s=size) 
    
    plt.show()
def main():
    np.random.seed(0)
    arr = np.random.randint(0, 10, (10, 4))  # 10 rows, 4 columns
    subfigures(arr)
    print("Sample array 'a':")
    print(a)

if __name__ == "__main__":
    main()
