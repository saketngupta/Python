def check_bal(bal):
    print(f"Current balance is :{bal}")
    
def dep(bal, amo):
    bal = bal + amo
    return bal

def withdraw(bal, amo):
    if amo <= bal:
        bal = bal - amo
        return bal
    else:
        print("Insufficient balance")
        return bal
        
bal = 5000

while True:
    print("1. check balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")
    choice = input("Enter your choice: ").strip()

    try:
        ch = int(choice)
    except ValueError:
        print("Invalid choice")
        continue
    
    if ch == 1:
        check_bal(bal)
        
    elif ch == 2:
        amo = int(input("Enter the amount: "))
        bal = dep(bal, amo)
        
    elif ch == 3:
        amo = int(input("Enter the amount: "))
        bal = withdraw(bal, amo)
        
    elif ch == 4:
        print("Thank you")
        break
    
    else:
        print("Invalid choice")   
        
