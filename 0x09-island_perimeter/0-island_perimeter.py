#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Calculate perimter of island
    """
    perimeter = 0

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
            if val == 1:
                perimeter += check_sides(x, y, grid)

    return perimeter


def check_sides(x, y, grid):
    """
    Check closed sides on given island
    """
    closed_sides = 0
    sides = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for side in sides:
        x_diff = x + side[0]
        y_diff = y + side[1]
        if (x_diff < 0 or x_diff >= len(grid) or
            y_diff < 0 or y_diff >= len(grid[0]) or
                grid[x_diff][y_diff] == 0):
            closed_sides += 1

    return closed_sides
