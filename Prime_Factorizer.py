n = int(input("Enter a number: "))

factor = 2

print("Prime factors:", end=" ")

while n > 1:
    if n % factor == 0:
        print(factor, end=" ")
        n //= factor
    else:
        factor += 1