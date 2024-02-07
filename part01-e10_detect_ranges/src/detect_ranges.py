def detect_ranges(L):
    # Make a copy of the input list to avoid modifying it
    sorted_list = sorted(L)
    
    result = []
    i = 0
    
    # Iterate over the sorted list
    while i < len(sorted_list):
        start = sorted_list[i]
        end = start + 1
        
        # Find the end of the interval
        while i + 1 < len(sorted_list) and sorted_list[i + 1] == end:
            i += 1
            end += 1
        
        # Append single number or interval tuple to the result list
        if start == end - 1:
            result.append(start)
        else:
            result.append((start, end))
        
        # Move to the next non-consecutive number
        i += 1
    
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    print(detect_ranges(L))

if __name__ == "__main__":
    main()
