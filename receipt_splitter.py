items = []

print("Enter items. Type 'done' when finished.\n")

while True:
    name = input("Item: ")

    if name.lower() == "done":
        break

    price = float(input("Price: ₹"))
    items.append((name, price))


people = int(input("\nNumber of people: "))
tip = float(input("Tip percentage: "))

subtotal = sum(price for _, price in items)
tip_amount = subtotal * tip / 100
total = subtotal + tip_amount
share = total / people


print("\n========== RECEIPT ==========")

for name, price in items:
    print(f"{name:<20} ₹{price:.2f}")

print("-----------------------------")
print(f"Subtotal:             ₹{subtotal:.2f}")
print(f"Tip:                  ₹{tip_amount:.2f}")
print(f"Total:                ₹{total:.2f}")
print(f"Each person pays:     ₹{share:.2f}")