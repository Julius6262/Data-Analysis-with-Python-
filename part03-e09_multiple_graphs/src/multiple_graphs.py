#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def main():
    x1 = np.array([2,4,6,7])
    y1 = np.array([4,3,5,1])

    x2 = np.array([1,2,3,4])
    y2 = np.array([4,2,3,1])

    plt.plot(x1,y1)  # plot points in  
    plt.plot(x2,y2)  # can also be done as (x1,y1,x2,y2) instead of two plot function calls
    plt.title("my first title")  # Adds title to graph
    plt.xlabel("my x-axis")  # give name to x-axis
    plt.ylabel("my y-axis")  # give name to y-axis
    plt.show()              # tell matplotlib to show the graph

if __name__ == "__main__":
    main()
