"""Day18 30 days of Python Programming"""

import re

def is_valid_variable(name):
    pattern=r"^[a-zA-Z_]+\d*"
    return True if re.fullmatch(pattern, name) != None else False

print(is_valid_variable("first_name"))
print(is_valid_variable("first-name"))
print(is_valid_variable("1first_name"))
print(is_valid_variable("firstname"))
