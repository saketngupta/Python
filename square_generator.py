n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Number must be odd.")
    exit()

square = [[0] * n for _ in range(n)]

row = 0
col = n // 2

for number in range(1, n * n + 1):

    square[row][col] = number

    new_row = (row - 1) % n
    new_col = (col + 1) % n

    if square[new_row][new_col]:
        row = (row + 1) % n
    else:
        row = new_row
        col = new_col

for row in square:
    print(" ".join(f"{x:2}" for x in row))