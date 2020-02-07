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


def slope(x1, y1, x2, y2):
    if x2 == x1:
        return None
    m = (y2 - y1) / (x2 - x1)
    return m


print(line_func(
    [[1, 1], [1, 2], [2, 2], [1, 3], [3, 3], [1, 4], [1, 5], [2, 6], [3, 9], [5, 8], [7, 3], [2, 4],
     [4, 5],
     [6, 6]]))

# TestCase: 2
print(line_func([[2, 6], [3, 9], [5, 8], [7, 3], [2, 4], [4, 5], [6, 6]]))

# TestCase: 3
print(line_func(
    [[0, 0], [11, 222], [21, 2], [11, 3], [32, 32], [11, 44], [122, 533], [2, 6], [3, 9], [5, 8],
     [7, 3], [2, 4],
     [4, 5],
     [6, 6]]))


def line_slope_and_intercept(l1, l2):
    if l2[0] - l1[0] != 0:
        m = (l2[1] - l1[1]) / (l2[0] - l1[0])
        c = (l2[1] - (m * l2[0]))

        return (m, c)


"""

The function 'solution_fast' takes in a list of coordinates of two dimensional space and returns a list of 
equations of lines which passes through three or more points from the given coordinates.

This function has a time complexity of O(n^2).

For any given point, I am trying to calculate the slope with all the other points and I am storing in a HashMap with the
slope as a key and the list of points as it's value. Now if the value of a HashMap has more than one value, it means 
that three points are collinear. This can be extended to find any number of collinear points.

"""


def solution_fast(list_of_coordinates):
    final_list_of_equations = set()
    for i in list_of_coordinates:
        temp_list = []
        hash_map = {}
        for j in list_of_coordinates:

            if i != j:

                if slope(i[0], i[1], j[0], j[1]) not in hash_map:
                    hash_map[slope(i[0], i[1], j[0], j[1])] = [j]
                else:
                    temp = hash_map[slope(i[0], i[1], j[0], j[1])]
                    temp.append(j)
                    hash_map[slope(i[0], i[1], j[0], j[1])] = temp

                temp_list.append(slope(i[0], i[1], j[0], j[1]))
        # print(temp_list)
        # print(hash_map)

        # iterating over the HashMap

        for key, value in hash_map.items():
            if len(value) > 1:
                a = value[0]
                b = value[1]
                final_list_of_equations.add(line_slope_and_intercept(a, b))
    return final_list_of_equations


print(solution_fast(
    [[1, 1], [1, 2], [2, 2], [1, 3], [3, 3], [1, 4], [1, 5], [2, 6], [3, 9], [5, 8], [7, 3], [2, 4],
     [4, 5],
     [6, 6]]))

# TestCase: 2
print(solution_fast([[2, 6], [3, 9], [5, 8], [7, 3], [2, 4], [4, 5], [6, 6]]))

# TestCase: 3
print(solution_fast(
    [[0, 0], [11, 222], [21, 2], [11, 3], [32, 32], [11, 44], [122, 533], [2, 6], [3, 9], [5, 8],
     [7, 3], [2, 4],
     [4, 5],
     [6, 6]]))
