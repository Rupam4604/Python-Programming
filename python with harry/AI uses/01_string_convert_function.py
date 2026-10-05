def clean_string(text):
    result = ""

    for char in text:
        if char.isalnum():
            result += char
        else:
            result += "_"

    return result


# Example 1
print(clean_string("hey how are you !"))

# Example 2
print(clean_string("Hello World"))

# Example 3
print(clean_string("Python is awesome!"))

# Example 4
print(clean_string("I am 22 years old."))

# Example 5
print(clean_string("Hello@Python#2026"))

# Example 6
print(clean_string("C++ is fun & powerful!"))


# 2nd way 

import re

def clean_string(text):
    return re.sub(r'[^a-zA-Z0-9]', '_', text)


# Examples
print(clean_string("hey how are you !"))
print(clean_string("Hello World"))
print(clean_string("Python is awesome!"))
print(clean_string("I am 22 years old."))
print(clean_string("Hello@Python#2026"))
print(clean_string("C++ is fun & powerful!")) 