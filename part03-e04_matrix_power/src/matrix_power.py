import numpy as np
from functools import reduce

def matrix_power(arr, n):
    if n == 0:
        return np.eye(len(arr))  # Return the identity matrix if n is 0
    
    elif n > 0:
        return reduce(np.matmul, [arr] * n)  # Perform matrix multiplication 'n' times
    
    else:  # For negative powers
        arr_inv = np.linalg.inv(arr)
        return reduce(np.matmul, [arr_inv] * (-n))  # Perform matrix multiplication 'n' times with the inverse





def main():
    # Example usage:
    arr = np.array([[1, 2],
                    [3, 4]])

    print(matrix_power(arr, 3))  # Raises matrix 'arr' to the power of 3
    print(matrix_power(arr, -1))  # Raises matrix 'arr' to the power of -1

if __name__ == "__main__":
    main()
