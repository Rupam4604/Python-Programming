# Write a Python program that:

# Takes the user's name
# Takes their age
# Prints their name and age
# Then calculates what their age will be after 5 years


# Example
# Enter your name: Rupam
# Enter your age: 22

# Hello Rupam!
# You are currently 22 years old.
# After 5 years, you will be 27 years old.


name = input("Enter your name: ")
age = int(input("Enter your Age: "))
print(f"{name} is {age} years old")
print(f"After 5 years the age will be {age + 5}")
