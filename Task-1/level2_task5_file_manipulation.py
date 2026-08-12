# Level 2 - Task 5: File Manipulation

from collections import Counter
import re

with open("sample.txt", "r") as file:
    text = file.read()

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

word_count = Counter(words)

print("Word Occurrences:")

for word in sorted(word_count):
    print(f"{word}: {word_count[word]}")