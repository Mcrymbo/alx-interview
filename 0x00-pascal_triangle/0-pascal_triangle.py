#!/usr/bin/python3
"""
function for developing pascal's triangle
"""

def pascal_triangle(n):
    """ function for pascal triagle """
    if n <= 0:
        return []
    pascal = [[] for idx in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if (col < row):
                if (col == 0):
                    pascal[row].append(1)
                else:
                    pascal[row].append(pascal[row - 1][col] + pascal[row - 1][col - 1])
            elif (col == row):
                pascal[row].append(1)

    return pascal
