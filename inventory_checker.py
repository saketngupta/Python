items = {}

while True:
    print("\n1. Add item")
    print("2. View inventory")
    print("3. Check item")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Item name: ").lower()
        quantity = int(input("Quantity: "))

        items[name] = items.get(name, 0) + quantity
        print("Item added!")

    elif choice == "2":
        print("\n--- Inventory ---")

        for name, quantity in items.items():
            print(f"{name}: {quantity}")

    elif choice == "3":
        name = input("Search item: ").lower()

        if name in items:
            print(f"{name}: {items[name]} available")
        else:
            print("Item not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")