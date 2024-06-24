#5. Find all three, four, and five character words in a string
import re

def find_words(text):
    pattern = r'\b\w{3,5}\b'
    return re.findall(pattern, text)

text = "Find all three, four, and five character words in a string."
print(find_words(text))  # Output: ['Find', 'all', 'four', 'and', 'five', 'words']
