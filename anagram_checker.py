a = input("First word: ").lower().replace(" ", "")
b = input("Second word: ").lower().replace(" ", "")

if sorted(a) == sorted(b):
    print("They are anagrams! ✅")
else:
    print("Not anagrams ❌")