#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    # Define the regular expression pattern to find integers enclosed in brackets
    pattern = r'\[(\s*[-+]?\d+\s*)\]'
    # Use re.findall to find all matches of the pattern in the input string
    matches = re.findall(pattern, s)
    # Convert the matched strings to integers and return them
    return list(map(int, matches))

def main():
    s = " afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    result = integers_in_brackets(s)
    print(result)  # Output: [12, -43, 12]



if __name__ == "__main__":
    main()
