#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
    row_vectors = []
    for row in a:

        row_shape = row.reshape(1,-1)  # extra [] to show it is a row vector
        row_vectors.append(row_shape)
    
    return row_vectors

def get_column_vectors(a):
    list_colum = []

    for col in a.T:
        col_shape = col.reshape(-1,1)
        list_colum.append(col_shape)

    return list_colum

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:")
    print(a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
