import re as r
from collections import defaultdict

text = "Either we we we retake the the the launch facility or we won’t recognize the world tomorrow. ah-ah"

min_occurrences = 3
words = r.findall(r'\b[\w\'\-а-яёА-ЯЁ]+\b', text.lower())
word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1
frequent_words = {word for word, count in word_counts.items() if count > min_occurrences}
code_table = {word: str(i) for i, word in enumerate(frequent_words, 1)}


def replace_match(match):
    wordLow = match.group(0).lower()
    wordOr=match.group(0)   
    return code_table.get(wordLow, wordOr)


compressed_text = r.sub(r'\b[\w\'\-а-яёА-ЯЁ]+\b', replace_match, text, flags=r.IGNORECASE)
print(text)
print(compressed_text)
print(code_table)
