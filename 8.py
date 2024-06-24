#8. Concatenate the consecutive numbers in a given string
import re

def concatenate_numbers(text):
    pattern = re.compile(r'(?<=\d) (?=\d)')
    return pattern.sub('', text)

text = "Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready."
print(concatenate_numbers(text))
