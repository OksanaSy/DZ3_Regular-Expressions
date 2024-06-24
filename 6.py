#6. Convert a camel-case string to a snake-case string

import re

def camel_to_snake(camel_str):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', camel_str).lower()

camel_str = "camelCaseString"
print(camel_to_snake(camel_str))
