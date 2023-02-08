"""
Determine if a triangle is equilateral, isosceles, or scalene. 
Inputs: equilateral, isosceles, scalene with parameter sides as a list of 3 numbers
Output: True or False
"""


def equilateral(sides):
    if sum(sides) == 0:
        return False
    # confirm all sides are the same length
    return len(set(sides)) == 1


def isosceles(sides):
    # confirm this is a triangle and that at least 2 sides are the same length
    return triangleCheck(sides) and len(set(sides)) <= 2


def scalene(sides):
    # confirm this is a triangle and that each side has a unique length
    return triangleCheck(sides) and len(set(sides)) == 3


def triangleCheck(sides):
    # confirm this is in fact a triangle given the lengths in sides
    # the all function creates a list of bools and only if all are True, returns True
    return all(side < sum(sides) - side for side in sides)


"""
def equilateral(sides):
    if sum(sides) == 0:
        return False
    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    else:
        return False


def isosceles(sides):
    sides.sort()
    if triangleCheck(sides) == True:
        if sides[1] == sides[2]:
            return True
        if sides.count(sides[1]) == 1:
            return False
    else:
        return False


def scalene(sides):
    sides.sort()
    if sides.count(sides[1]) > 1:
        return False
    if triangleCheck(sides) == True:
        return True
    else:
        return False


def triangleCheck(sides):
    if (
        sides[0] + sides[1] >= sides[2]
        and sides[1] + sides[2] >= sides[0]
        and sides[0] + sides[2] >= sides[1]
    ):
        return True
    else:
        return False

"""

isosceles([1, 1, 3])

