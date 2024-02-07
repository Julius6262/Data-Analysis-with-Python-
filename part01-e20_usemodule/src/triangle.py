# Enter you module contents here
import math

__author__ = "Martin J"
__version__ = "1.0"
__doc__ = "This module contains functions for calculating the hypotenuse and area of right-angled triangle"

def hypotenuse(side1: float, side2: float) -> float:
    """
    Calculate the length of the hypotenuse of a right-angled triangle.

    Parameters:
        side1 (float): The length of one of the sides of the triangle.
        side2 (float): The length of the other side of the triangle.

    Returns:
        float: The length of the hypotenuse.
    """
    
    return math.sqrt(side1**2 + side2**2)

    

def area(base: float, height: float) -> float:
    
    """
    Calculate the area of a right-angled triangle.

    Parameters:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle, perpendicular to the base.

    Returns:
        float: The area of the triangle.
    """
    
    return 0.5 * base * height