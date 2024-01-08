#!/usr/bin/python3
"""pascal triangle task"""


def pascal_triangle(n):
    """returns a list of integers representing pascal's triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    prev_row = [1]

    for i in range(1, n):
        base_row = [1]

        for j in range(1, len(prev_row)):
            num = prev_row[j] + prev_row[j - 1]
            base_row.append(num)
        base_row.append(1)
        triangle.append(base_row)
        prev_row = base_row
    
    return triangle
