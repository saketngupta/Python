import re

text = input("Paste some text: ")

urls = re.findall(
    r'https?://[^\s]+',
    text
)

if urls:
    print("\nFound URLs:")
    for url in urls:
        print(url)
else:
    print("No URLs found.")