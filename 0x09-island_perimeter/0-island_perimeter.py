#!/usr/bin/python3
"0-island-perimeter"


def island_perimeter(grid):
    """
    Calculate perimter of island
    """
    perimeter = 0

    for x, row in enumerate(grid):
        for val in row:
            if val == 1:
                perimeter += check_sides(x, val, grid)

    return perimeter


def check_sides(x, y, grid):
    """
    Check closed sides on given island
    """
    closed_sides = 0
    sides = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for side in sides:
        x_diff = x - side[0]
        y_diff = y - side[1]

        if len(grid) > x_diff >= 0 and len(grid) > y_diff >= 0:
            if grid[x_diff][y_diff] == 0:
                closed_sides += 1


    return closed_sides
