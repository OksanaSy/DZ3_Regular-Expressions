#1. Match a word containing 'z', not at the start or end of the word

def find_with_z(text):
    pattern = r'\b\w+z\w+\b'
    find = re.findall(pattern, text)
    return find

text = "Amazing pizza zone has zesty flavors.Saz."
print(find_with_z(text)) 
