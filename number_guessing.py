import random

number = random.randint(1, 20)

while True:
    guess = int(input("Guess (1-20): "))

    if guess == number:
        print("Correct!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")