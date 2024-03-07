#!/usr/bin/python3
#!/usr/bin/python3

import numpy as np
from numpy.linalg.linalg import LinAlgError

def almost_meeting_lines(a1, b1, a2, b2):
    """
    function
    y = a1*x + b1
    y = a2*x + b2

    We can represent this system of equations in matrix form:
    [a1 -1]  [x] = [-b] 
    [a2 -1]  [y] = [-b]
    
    Use the numpy.linalg.solve function to solve the system of equations.
    """
    
    A = np.array([[a1, -1], [a2, -1]])
    B = np.array([-b1, -b2])
    varibles = None
    try:
        varibles = np.linalg.solve(A,B)
        return (varibles, True)
    except LinAlgError:
        varibles = np.linalg.lstsq(A,B)[0]  # if no excat point get the cloest point
        return (varibles, False)

def main():
    a1=1
    b1=2
    a2=-1
    b2=0

    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")

    a1=a2=1
    b1=2
    b2=-2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    (x, y), exact = almost_meeting_lines(a1, b1, a1, b1)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

    a1=1
    b1=2
    a2=1
    b2=1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    if exact:
        print(f"Lines meet at x={x} and y={y}")
    else:
        print(f"Closest point at x={x} and y={y}")

if __name__ == "__main__":
    main()
