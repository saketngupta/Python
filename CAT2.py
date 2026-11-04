cart = []

while True:
    print("CART")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update item")
    print("4. Show bill")
    print("5. exit")
    ch = int(input("Enter a choice: "))
    
    if ch == 1:
        name = input("Enter the name: ")
        price = float(input("Enter the price: "))
        item = {
            "name" : name,
            "price" : price
        }
        cart.append(item)
    
    elif ch == 2:
        name = input("Enter the name: ")
        for item in cart:
            if item["name"] == name:
                cart.remove(item)
                print("Item removed.")
                break
        else:
            print("Item not found.")
    
    elif ch == 3:
        name = input("Enter the name of item you want to update: ")
        for item in cart:
            if item["name"] == name:
                new = float(input("Enter the new price: "))
                item["price"] = new
        else:
            print("Item not found.")
                
    elif ch == 4:
        total = 0
        print("Items in cart: ")
        for item in cart:
            print(item["name"], "=", item["price"])
            total = total + item["price"]
        print(f"Total bill: {total}")
        
        if total >= 500:
            dis = total * 0.10
            total = total - dis
        print(f"Total :{total}")
        print(f"Discount: {dis}")
        
    elif ch == 5:
        print("Thank you")
        break
    
    else:
        print("Invalid input")
        
