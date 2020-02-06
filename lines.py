import itertools
from decimal import Decimal

final_list = []

"""
The function 'is_collinear' checks if the three given points on two dimensional space are collinear or not.
The function finds the area of a triangle and if the area is zero then the lines are collinear and returns true and vice 
versa.
"""


def is_collinear(list_of_three_points):
    x1 = list_of_three_points[0][0]
    y1 = list_of_three_points[0][1]
    x2 = list_of_three_points[1][0]
    y2 = list_of_three_points[1][1]
    x3 = list_of_three_points[2][0]
    y3 = list_of_three_points[2][1]

    area_of_triangle = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if area_of_triangle == 0:
        return True

    return False


"""
The function 'line_equation' returns the equation of a line for any given two points.
"""


def line_equation(l1, l2):
    if l2[0] - l1[0] != 0:
        m = Decimal((l2[1] - l1[1])) / Decimal(l2[0] - l1[0])
        c = (l2[1] - (m * l2[0]))
        # print("y = " + str(m) + "x + " + str(c))
        final_list.append("y = " + str(m) + "x + " + str(c))

    else:
        # print("x = " + str(l2[0]))
        final_list.append("x = " + str(l2[0]))


"""
The function 'line_func' takes in a list of coordinates of two dimensional space and returns a list of 
equations of lines which passes through three or more points from the given coordinates.
"""


def line_func(list_of_coordinates):
    final_list.clear()

    for i in itertools.combinations(list_of_coordinates, 3):

        if is_collinear(i):
            # print(i)
            # print("collinear")
            line_equation(i[0], i[1])

    if len(set(final_list)) == 0:
        print("No line passes through three or more points from the given coordinates")

    return set(final_list)


# TestCase: 1
print(line_func([[1, 1], [1, 2], [2, 2], [1, 3], [3, 3], [1, 4], [1, 5], [2, 6], [3, 9], [5, 8], [7, 3], [2, 4], [4, 5],
                 [6, 6]]))

# TestCase: 2
print(line_func([[2, 6], [3, 9], [5, 8], [7, 3], [2, 4], [4, 5], [6, 6]]))

# TestCase: 3
print(line_func(
    [[0, 0], [11, 222], [21, 2], [11, 3], [32, 32], [11, 44], [122, 533], [2, 6], [3, 9], [5, 8], [7, 3], [2, 4],
     [4, 5],
     [6, 6]]))
