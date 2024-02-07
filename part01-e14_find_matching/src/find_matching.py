#!/usr/bin/env python3

def find_matching(L: list, pattern: str) -> list:
    return [index for index, element in enumerate(L) if pattern in element]

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
