#!/usr/bin/env python3

import re

def red_green_blue():
    # Define the pattern to match each line
    pattern = r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)'
    result = []

    # Open the file and read each line
    with open('src/rgb.txt', 'r') as file:
        # Skip the first line
        next(file)
        for line in file:
            # Match the pattern in each line
            match = re.match(pattern, line.strip())
            if match:
                # Rearrange the components with tabs and add to result
                cleaned_line = '\t'.join(match.groups())
                result.append(cleaned_line)

    return result

# Test if the function is called
def test_called():
    red_green_blue()


def main():
    red_green_blue()

if __name__ == "__main__":
    main()
