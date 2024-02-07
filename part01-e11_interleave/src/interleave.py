#!/usr/bin/env python3

def interleave(*lists):
    
    interleaved = []
    for zipped in zip(*lists):
        interleaved.extend(zipped)
    return interleaved
def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
