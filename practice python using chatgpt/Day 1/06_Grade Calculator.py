# Grade Calculator

# Now we're going to make your conditions more complex.

# Write a program that takes a student's percentage and prints their grade according to this system:

# Percentage	Grade
# 90–100	A+
# 80–89	A
# 70–79	B
# 60–69	C
# 50–59	D
# 40–49	E
# Below 40	F
# Example
# Enter percentage: 87

# Percentage: 87%
# Grade: A

# Another:

# Enter percentage: 35

# Percentage: 35%
# Grade: F

# Challenge

# Also handle an invalid percentage:

# Enter percentage: 125

# Invalid percentage!

# A valid percentage must be between 0 and 100.

# Method 1

'''

percentage = int(input("Enter the percentage: "))

if 0 <= percentage <= 100:
    if 100 >= percentage >= 90:
        grade = "A+"
    elif 89 >= percentage >=80:
        grade = "A"
    elif 79 >= percentage >=70:
        grade = "B"
    elif 69 >= percentage >=60:
        grade = "C"
    elif 59 >= percentage >=50:
        grade = "D"
    elif 49 >= percentage >=40:
        grade = "E"
    else :
        grade = "F"
    print(f" Percentage: {percentage:.2f}%\n Grade: {grade}")
else:
    print("error! Invalid percentage!")

'''
# method 2 

percentage = int(input("Enter the percentage: "))

if 0 <= percentage <= 100:
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    print(f" Percentage: {percentage}%\n Grade: {grade}")
else:
    print("error! Invalid percentage!")