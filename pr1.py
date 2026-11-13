import random 

thres = 25
temp = random.randint(10, 40)
print(f"Current temperature is: {temp}")
if temp > thres:
    print("HIGH TEMP")
else:
    print("NORMAL")