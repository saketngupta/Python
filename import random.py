import random

SIZE = 4
board = [[0] * SIZE for _ in range(SIZE)]
score = 0


def add_tile():
    empty = []

    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                empty.append((r, c))

    if empty:
        r, c = random.choice(empty)
        board[r][c] = 2


def print_board():
    print("\nScore:", score)
    print("-" * 25)

    for row in board:
        for num in row:
            if num == 0:
                print(".", end="\t")
            else:
                print(num, end="\t")
        print()

    print("-" * 25)


def compress(row):
    new = [x for x in row if x != 0]

    i = 0
    while i < len(new) - 1:
        if new[i] == new[i + 1]:
            new[i] *= 2
            global score
            score += new[i]
            new.pop(i + 1)
        i += 1

    while len(new) < SIZE:
        new.append(0)

    return new


def move_left():
    for i in range(SIZE):
        board[i] = compress(board[i])


def move_right():
    for i in range(SIZE):
        board[i].reverse()
        board[i] = compress(board[i])
        board[i].reverse()


def move_up():
    for c in range(SIZE):
        column = []

        for r in range(SIZE):
            column.append(board[r][c])

        column = compress(column)

        for r in range(SIZE):
            board[r][c] = column[r]


def move_down():
    for c in range(SIZE):
        column = []

        for r in range(SIZE):
            column.append(board[r][c])

        column.reverse()
        column = compress(column)
        column.reverse()

        for r in range(SIZE):
            board[r][c] = column[r]


add_tile()
add_tile()

while True:

    print_board()

    move = input("Move (W/A/S/D) or Q to quit: ").lower()

    if move == "a":
        move_left()
    elif move == "d":
        move_right()
    elif move == "w":
        move_up()
    elif move == "s":
        move_down()
    elif move == "q":
        break
    else:
        print("Invalid move!")
        continue

    add_tile()