#!/usr/bin/env python3

def transform(s1: list, s2: list)-> list:
    s1 = s1.split()
    s2 = s2.split()
    s1 = list(map(int,s1))
    s2 = list(map(int,s2))

    zipper = list(zip(s1,s2))
    return  [s[0]*s[1] for s in zipper]
    

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
