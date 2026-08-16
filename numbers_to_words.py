ones = [
    "zero", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine"
]

teens = [
    "ten", "eleven", "twelve", "thirteen",
    "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty",
    "ninety"
]


def words(n):
    if n < 10:
        return ones[n]

    if n < 20:
        return teens[n - 10]

    if n < 100:
        return tens[n // 10] + (
            "" if n % 10 == 0
            else " " + ones[n % 10]
        )

    if n < 1000:
        return (
            ones[n // 100]
            + " hundred"
            + (
                "" if n % 100 == 0
                else " " + words(n % 100)
            )
        )

    if n < 1000000:
        return (
            words(n // 1000)
            + " thousand"
            + (
                "" if n % 1000 == 0
                else " " + words(n % 1000)
            )
        )


number = int(input("Enter a number: "))

print(words(number))