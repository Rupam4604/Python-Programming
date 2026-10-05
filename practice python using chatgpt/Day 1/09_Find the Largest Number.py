# Find the Largest Number

# Now we're going to make your loop logic harder.

# Write a program that asks the user for 5 numbers and finds:

# The largest number
# The smallest number
# Example
# Enter number 1: 25
# Enter number 2: 10
# Enter number 3: 45
# Enter number 4: 7
# Enter number 5: 30

# Largest number: 45
# Smallest number: 7

i = 1



for i in range(1,6):
    num = int(input(f"Enter number {i}: "))
    if i == 1:
        current_large = num
        current_small = num
    
    if num > current_large:
        current_large = num
    else:
        current_large = current_large
    if  num < current_small:
        current_small = num
    else:
        current_small = current_small


print(f"Largest number: {current_large}\nSmallest number: {current_small}")