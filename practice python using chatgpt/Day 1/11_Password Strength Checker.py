# Password Strength Checker

# Ask the user to enter a password.

# Your program should check:

# Password length is at least 8 characters
# Contains at least one uppercase letter
# Contains at least one lowercase letter
# Contains at least one digit
# Contains at least one special character (@, #, $, %, !, etc.)

# Then print:

# Password Strength Report

# Length: PASS
# Uppercase: PASS
# Lowercase: PASS
# Digit: PASS
# Special Character: FAIL

# Password Strength: WEAK

# If all 5 conditions pass:

# Password Strength: STRONG


print('''
Welcome to Password Strength Checker:-

Password length is at least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Contains at least one special character (@, #, $, %, !, etc.)
''')
uppercase_found = False
lowercase_found = False
digit_found = False
special_found = False
length_valid = False



password = input("Enter your password: ")

if len(password) >= 8:
    length_valid = True

for char in password:
    if char.isupper():
        uppercase_found = True
  
    if char.islower():
        lowercase_found= True

    if char.isdigit():
        digit_found= True

    if not char.isalnum():
        special_found= True

    
   

if uppercase_found:
    print("Uppercase: pass")
else:
    print("Uppercase: fail")
    
if lowercase_found:
    print("lowercase: pass")
else:
    print("lowercase: fail")

if digit_found:
    print("Digit: pass")
else:
    print("Digit: fail")

if  special_found:
    print("Special Character: pass")
else:
    print("Special Character: fail")

if length_valid:
    print("length: pass")
else:
    print("length: fail")

if length_valid and uppercase_found and lowercase_found and digit_found and special_found :
    print("Password Strength: STRONG")
else:
    print("Password Strength: WEAK")