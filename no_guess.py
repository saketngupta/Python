correct = int(23)
while True:
    guess = int(input("Enter a no: "))
    if guess == correct:
        print("Correct")
        break
    else:
        print("Try again")

print(id(correct))