#!/usr/bin/env python3


def main():
    def triple(x):
        return x*3
    
    def square(x):
        return x**2

    for i in range(1,11):
        if triple(i) >= square(i):
            print(f"triple({i})=={triple(i)} square({i})=={square(i)}")



if __name__ == "__main__":
    main()
