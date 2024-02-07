#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    else:
        string_list = list(map(str,L))
        plus_list = " + ".join(string_list)
        return f"{plus_list} = {sum(L)}"

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
