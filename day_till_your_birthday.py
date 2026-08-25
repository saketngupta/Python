from datetime import date

day = int(input("Birth day: "))
month = int(input("Birth month: "))

today = date.today()
birthday = date(today.year, month, day)

if birthday < today:
    birthday = date(today.year + 1, month, day)

days_left = (birthday - today).days

print(f"Only {days_left} days until your birthday! 🎉")