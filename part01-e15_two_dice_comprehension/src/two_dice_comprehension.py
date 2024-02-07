#!/usr/bin/env python3

def main():
    number_of_five = [print((d_1,d_2)) for d_1 in range(1,7)
                                for d_2 in range(1,7)
                                if d_1+d_2 == 5 or d_2+d_1 == 5]

    


if __name__ == "__main__":
    main()
