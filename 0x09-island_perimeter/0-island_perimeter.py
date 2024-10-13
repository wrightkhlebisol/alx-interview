#!/usr/bin/python3
"""
Calculate perimter of island
"""
def island_perimeter(grid):
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                perimeter += check_sides(x,y,grid)
    return perimeter

"""
Check closed sides on given island
"""
def check_sides(x, y, grid):
    closed_sides = 0
    sides = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for side in sides:
        if grid[x - side[0]][y - side[1]] == 0:
            closed_sides += 1
    return closed_sides

