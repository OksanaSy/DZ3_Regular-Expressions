#1. Match a word containing 'z', not at the start or end of the word

def find_with_z(text):
    pat = r'\b\w+z\w+\b'
    find = re.findall(pat, text)
    return find

text = "Amazing pizza zone has zesty flavors.Saz."
print(find_with_z(text)) 
