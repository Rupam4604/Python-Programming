# Number Analyzer

# Write a program that asks the user for 5 numbers, one at a time.

# Your program should calculate:

# Sum of all 5 numbers
# Average
# How many numbers are even
# How many numbers are odd

# Display the results on the screen.

# Example
# Enter number 1: 10
# Enter number 2: 15
# Enter number 3: 8
# Enter number 4: 7
# Enter number 5: 20

# Sum: 60
# Average: 12.0
# Even numbers: 3
# Odd numbers: 2

# My solution

i = 1
even_count = 0
odd_count = 0
total = 0

for i in range(1, 6):
    num = int(input(f"Enter number {i}: "))
    i = i + 1
    total = total + num
    avearage = total / (i-1)
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

    

print(f"Sum: {total}\nAverage: {avearage}\nEven numbers: {even_count}\nOdd numbers: {odd_count}")


# improve correction(AI)

even_count = 0
odd_count = 0
total = 0

for i in range(1, 6):

    num = int(input(f"Enter number {i}: "))

    total = total + num

    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

average = total / 5

print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
