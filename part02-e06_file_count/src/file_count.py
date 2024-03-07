#!/usr/bin/env python3

import sys

def file_count(filename):
    wordcount = 0
    charactercount = 0
    with open(filename) as file:
        for linecount, line in enumerate(file, start=1):  # count lines from 1 with enumerate
            words = line.split()
            wordcount += len(words)
            charactercount += len(line)  # inclusiv space and punctuation
    
    return (linecount, wordcount, charactercount)  # number of lines, words, characters

def main():
    filenames = sys.argv[1:]
    for filename in filenames:
        linecount, wordcount, charactercount = (file_count(filename))
        print(f"{linecount}\t{wordcount}\t{charactercount}\t{filename}")


if __name__ == "__main__":
    main()
