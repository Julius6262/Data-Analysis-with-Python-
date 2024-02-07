#!/usr/bin/env python3

def distinct_characters(L: list):
    return {string: len(set(string)) for string in L}

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
