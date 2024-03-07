#!/usr/bin/python3

import numpy as np

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    
    """ 
        The following equations:
        a1y +b1x +c1 = z1
        a2y +b2x +c2 = z2
        a3y +b3x +c3 = z3

        can be put on the matrix form:
        [b1 a1 -1] [x] = [-c1]
        [b2 a2 -1] [y] = [-c2]
        [b3 a3 -1] [z] = [-c3]
    """
    
    # Coefficients matrix (A)
    A = np.array([[b1, a1, -1], [b2, a2, -1], [b3, a3, -1]])

    # Constants vector (b)
    b = np.array([-c1, -c2, -c3])

    # Solve the system of equations
    intersection_point = np.linalg.solve(A, b)  # x,y,z

    return intersection_point

def main():
    a1=1
    b1=4
    c1=5
    a2=3
    b2=2
    c2=1
    a3=2
    b3=4
    c3=1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")

if __name__ == "__main__":
    main()
