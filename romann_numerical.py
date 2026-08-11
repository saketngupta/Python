values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

roman = input("Enter Roman numeral: ").upper()

total = 0

for i in range(len(roman)):
    value = values[roman[i]]

    if i + 1 < len(roman) and value < values[roman[i + 1]]:
        total -= value
    else:
        total += value

print("Value:", total)