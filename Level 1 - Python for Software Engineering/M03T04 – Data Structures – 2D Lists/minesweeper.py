def adjacent_mines(row, col, grid):
    count = 0
    # Nested for loops to go through the adjacent cells
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (
                # Check out of range
                i < 0
                or j < 0
                or (i > len(grid) - 1)
                or (j > len(grid[0]) - 1)
                # On current item
                or (i == row and j == col)
            ):
                continue
            if grid[i][j] == "#":
                count += 1

    return count


# Start of program
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
]

rows = len(grid)
cols = len(grid[0])
row_output = []

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "#":
            row_output.append("#")
        else:
            number_mines = adjacent_mines(i, j, grid)
            row_output.append(str(number_mines))
    print(" ".join(row_output))
    row_output = []
