#!/usr/bin/env python3

from math import pi


def main():
    # enter you solution here
    while True:
        user_shape = input("Choose a shape (triangle, rectangle, circle): ")
        if user_shape =="":
            break
        
        elif user_shape == "triangle":
            user_base = float(input("Give base of the triangle: "))
            user_height = float(input("Give height of the triangle: "))
            print(f"The area is {(user_base*user_height)/2}")
        
        elif user_shape == "rectangle":
            user_width = float(input("Give width of the rectangle: "))
            user_height = float(input("Give height of the rectangle:"))
            print(f"The area is {(user_width*user_height)}")
        
        elif user_shape == "circle":
           user_circle = float(input("Give radius of the circle: "))
           print(f"The area is {user_circle**2 * pi}")

        else: print("Unknown shape!")
if __name__ == "__main__":
    main()
