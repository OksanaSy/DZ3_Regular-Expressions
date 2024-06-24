#7. Find all adverbs and their positions in a given sentence
import re

def find_adverbs(sentence):
    pattern = r'\b\w+ly\b'
    matches = [(match.group(), match.start(), match.end()) for match in re.finditer(pattern, sentence)]
    return matches

text = "He quickly ran and she softly spoke."
print(find_adverbs(text))
