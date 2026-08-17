text = input("Enter some text: ")

counts = {}

for char in text.lower():
    if char != " ":
        counts[char] = counts.get(char, 0) + 1

most_common = max(counts, key=counts.get)

print("Most common character:", most_common)
print("Occurrences:", counts[most_common])