for i in range(1, 8):
    if i % 2 == 0 and i > 3:
        print(i, "A")
    elif i % 3 == 0 or i == 1:
        print(i, "B")
    else:
        print(i, "C")        