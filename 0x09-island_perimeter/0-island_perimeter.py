#!/usr/bin/python3
""" Island Perimeter """

def island_perimeter(grid: list[list[int]]) -> int:
    """
    Returns the perimeter of the island described in grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 for each land cell
                perimeter += 4
                
                # Check the left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # One side is shared, so subtract 2
                
                # Check the top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # One side is shared, so subtract 2

    return perimeter
