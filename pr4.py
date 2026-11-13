feedback = "     moonlight homestay is an amazing amazing place to relax    "

def remove_spaces(text):
    text = text.strip()
    print(text)
    
def remove_duplicate(text):
    text = text.replace("amazing amazing", "amazing")
    print(text)
    
def capitalize_words(text):
    text = text.title()
    print(text)
    
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch == "aeiou":
            count += 1
    print(count)
    
def find_word(text):
    w = text.split()
    
    if "relax" in w:
        pos = w.index("relax") +1
        print(pos)
    else:
        print("word not found")
        
def join_words(text):
    w = text.split()
    print("-".join(w))
    
while True:
    print("\n--- Feedback Processing Menu ---")
    print("1. Remove extra spaces")
    print("2. Remove duplicate word")
    print("3. Capitalize each word")
    print("4. Count vowels")
    print("5. Find position of 'Relax'")
    print("6. Join words using '-'")
    print("7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        remove_spaces(feedback)
    elif choice == 2:
        remove_duplicate(feedback)
    elif choice == 3:
        capitalize_words(feedback)
    elif choice == 4:
        count_vowels(feedback)
    elif choice == 5:
        find_word(feedback)
    elif choice == 6:
        join_words(feedback)
    elif choice == 7:
        print("Thank you for using the feedback processor.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
    
