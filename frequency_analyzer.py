import re
from collections import Counter

text = input("Enter your text: ")

words = re.findall(r"[a-zA-Z]+", text.lower())

stop_words = {
    "the", "a", "an", "is", "are",
    "was", "were", "to", "of", "and",
    "in", "on", "for", "with", "it"
}

words = [
    word for word in words
    if word not in stop_words
]

counts = Counter(words)

print("\nMost common words:")

for word, count in counts.most_common(10):
    print(f"{word:<15} {count}")