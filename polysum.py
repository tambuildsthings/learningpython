"""
polysum by Tamgible
"""
import math


def polysum(n, s):
    """
        inputs: 
            n is the number of sides as an int, 
            s is the length of each side an int
        output: 
            sum of the area and square of the perimeter of the regular polygon, 
            rounded to 4 decimal places.

        Note: I'm using math.tan and math.pi so import math is essential
    """

    # calculate perimeter
    polyPerimeter = n * s

    # calculate area with (0.25*n*s^2)/tan(pi/n)
    polyArea = (0.25 * n * s ** 2) / math.tan(math.pi / n)

    # return the sum of the area and the square of the perimeter to 4 dec places
    return round(polyArea + (polyPerimeter ** 2), 4)


print(polysum(3, 4))

