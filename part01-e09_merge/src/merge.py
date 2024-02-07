#!/usr/bin/env python3

def merge(L1, L2):
    new_list = []
    i = 0  # Pointer for L1
    j = 0  # Pointer for L2

    # Traverse both lists and compare elements
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            new_list.append(L1[i])
            i += 1
        else:
            new_list.append(L2[j])
            j += 1

    # Append remaining elements of L1, if any
    while i < len(L1):
        new_list.append(L1[i])
        i += 1

    # Append remaining elements of L2, if any
    while j < len(L2):
        new_list.append(L2[j])
        j += 1

    return new_list

def main():
    pass

if __name__ == "__main__":
    main()
