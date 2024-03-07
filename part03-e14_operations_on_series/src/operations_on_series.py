#!/usr/bin/env python3
import pandas as pd

def create_series(list1, list2):  #len = 3
    s1 = pd.Series(list1, index=["a", "b","c"])
    s2 = pd.Series(list2, index=["a", "b","c"])
    return (s1, s2)
    
def modify_series(s1, s2):
    # Retrieve the value from s2 with index 'b'
    value_d = s2["b"]
    
    # Remove the element with index 'b' from s2
    s2 = s2.drop("b")
    
    # Add the retrieved value to s1 with a new index 'd'
    s1["d"] = value_d
    
    return s1, s2


    
def main():
    s1, s2 = create_series([1, 2, 3], [2, 4, 6])
    
    # Modify the series and print the result
    modified_s1, modified_s2 = modify_series(s1, s2)
    print("Modified s1:")
    print(modified_s1)
    print("\nModified s2:")
    print(modified_s2)
    
    # Add together the modified Series
    added_series = modified_s1 + modified_s2
    print("\nAdded Series:")
    print(added_series)
    
if __name__ == "__main__":
    main()
