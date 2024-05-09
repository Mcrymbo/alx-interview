#!/usr/bin/python3
""" calculates the perimeter of an ispland descibed in grid
"""


def island_perimeter(grid):
    ''' function that returns perimeter of an island '''

    if not grid:
        return

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # checking left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                # checking top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
