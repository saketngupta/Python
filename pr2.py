for _ in range(3):
    sig = input("Enter Signal (RED/GREEN/YELLOW): ")
    
    if sig == "RED":
        print("STOP")
    elif sig == "YELLOW":
        print("SLOW DOWN")
    elif sig == "GREEN":
        print("GO")
    else: 
        print("WRONG INPUT")