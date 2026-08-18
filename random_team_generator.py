import random

names = input("Enter names(comma seprated): ").split(",")
size = int(input("People per team: "))

names = [name.strip() for name in names]
random.shuffle(names)

for i in range(0, len(names), size):
    team = names[i:i + size]
    print(f"Team {i // size + 1}:",",".join(team))
    