#!/usr/bin/python3

import numpy as np

def meeting_lines(a1, b1, a2, b2):
    """
    function
    y = a1*x + b1
    y = a2*x + b2

    We can represent this system of equations in matrix form:
    [a1 -1]  [x] = [-b] 
    [a2 -1]  [y] = [-b]
    
    Use the numpy.linalg.solve function to solve the system of equations.
    """
    # Create the matrix
    A = np.array([[a1, -1], [a2, -1]])
    # Create the vector
    b = np.array([[-b1], [-b2]])
    # Solve the system
    x = np.linalg.solve(A, b)
    return x

def main():
    a1=1
    b1=4
    a2=3
    b2=2

    x, y  = meeting_lines(a1, b1, a2, b2)
    print(f"Lines meet at x={x} and y={y}")

if __name__ == "__main__":
    main()
