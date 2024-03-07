import numpy as np

def most_frequent_first(arr, col_index):
    # Extract the specified column
    col = arr[:, col_index]
    
    # Compute element frequencies
    unique_elements, element_counts = np.unique(col, return_counts=True)
    
    # Sort unique elements based on counts
    sorted_indices = np.argsort(element_counts)[::-1]
    sorted_elements = unique_elements[sorted_indices]
    
    # Initialize result array
    result = np.empty_like(arr)
    index = 0
    
    # Concatenate rows for each unique element in the specified order
    for element in sorted_elements:
        # Find indices of rows where the element occurs
        indices = np.where(col == element)[0]
        # Concatenate rows to result array
        result[index:index+len(indices)] = arr[indices]
        index += len(indices)
    
    return result

# Example usage
a = np.array([[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
              [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
              [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
              [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
              [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
              [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
              [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
              [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
              [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
              [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]])

result = most_frequent_first(a, -1)
print(result)
