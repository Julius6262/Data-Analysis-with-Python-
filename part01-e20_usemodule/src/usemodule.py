#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    print(triangle.hypotenuse.__doc__)
    print(triangle.area.__doc__)
    print(triangle.__doc__)

if __name__ == "__main__":
    main()
