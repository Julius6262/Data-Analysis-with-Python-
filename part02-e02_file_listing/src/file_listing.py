#!/usr/bin/env python3
import re


def file_listing(filename="src/listing.txt"):
    file_data = []
    with open(filename) as file:
        for line in file:
            pattern = r"^\S+\s+\S+\s+\S+\s+\S+\s+(\d+)\s+(\w{3})\s+(\d{1,2})\s+(\d{1,2}):(\d{2})\s+(.+)$"
            match = re.match(pattern, line)
            
            # If match is found, extract the required data and append it to the result list
            if match:
                size, month, day, hour, minute, filename = match.groups()
                file_data.append((int(size), month, int(day), int(hour), int(minute), filename))
    return file_data

def main():
    pass

if __name__ == "__main__":
    main()
