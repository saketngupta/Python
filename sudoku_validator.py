grid = []

print("Enter 9 rows of Sudoku:")

for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)


def valid_group(values):
    values = [x for x in values if x != 0]
    return len(values) == len(set(values))


valid = True

# Rows
for row in grid:
    if not valid_group(row):
        valid = False

# Columns
for col in range(9):
    values = [grid[row][col] for row in range(9)]
    if not valid_group(values):
        valid = False

# 3x3 boxes
for r in range(0, 9, 3):
    for c in range(0, 9, 3):

        box = []

        for i in range(r, r + 3):
            for j in range(c, c + 3):
                box.append(grid[i][j])

        if not valid_group(box):
            valid = False


print(
    "Valid Sudoku ✅"
    if valid
    else "Invalid Sudoku ❌"
)