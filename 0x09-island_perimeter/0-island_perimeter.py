#!/usr/bin/python3
""" Island Perimeter """

def island_perimeter(grid) -> int:
    """
    Returns the perimeter of the island described in grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
                
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
