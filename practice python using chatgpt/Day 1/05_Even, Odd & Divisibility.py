# Even, Odd & Divisibility

# Write a Python program that takes one integer from the user and determines:

# Whether it is positive, negative, or zero
# If it is positive, determine whether it is even or odd
# If it is positive, check whether it is divisible by 5
# Example 1
# Enter a number: 20

# Number: 20
# Type: Positive
# Even/Odd: Even
# Divisible by 5: Yes
# Example 2
# Enter a number: 17

# Number: 17
# Type: Positive
# Even/Odd: Odd
# Divisible by 5: No
# Example 3
# Enter a number: -8

# Number: -8
# Type: Negative
# Example 4
# Enter a number: 0

# Number: 0
# Type: Zero


num = int(input("Enter a number: "))

if num > 0:
    num_type = "positive"
    if num % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"

    if num % 5 == 0:
        divisible = "YES"
    else:
        divisible ="No"

    print(f" Number: {num}\n Type: {num_type}\n Even/odd: {even_odd}\n Divisible by 5: {divisible}")
    
elif num < 0:
    num_type = "Negative"
    print(f" Number: {num}\n Type: {num_type}")
else:
    num_type = "Zero"
    print(f" Number: {num}\n Type: {num_type}")


    


