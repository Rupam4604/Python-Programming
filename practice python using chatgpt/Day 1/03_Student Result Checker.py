# Student Result Checker

# Write a Python program that asks the user for marks in three subjects:

# Physics
# Mathematics
# Electronics

# Then calculate:

# Total marks
# Percentage

# Assume each subject is out of 100.

# Then display whether the student passed or failed.

# Rule

# A student passes only if their percentage is 40% or above.

# Example
# Enter Physics marks: 70
# Enter Mathematics marks: 80
# Enter Electronics marks: 65

# Total Marks: 215
# Percentage: 71.67%
# Result: PASS

# Another example:

# Enter Physics marks: 30
# Enter Mathematics marks: 55
# Enter Electronics marks: 35

# Total Marks: 120
# Percentage: 40.00%
# Result: PASS


#METHOD 1

physics = float(input("Enter the marks out of 100 : "))
mathematics = float(input("Enter the marks out of 100 : "))
electronics = float(input("Enter the marks out of 100 : "))

total_marks = physics + mathematics +electronics
percentage = (total_marks / 300) * 100

print(f'''
REPORT CARD
TOTAL MARKS: {total_marks}
PERCENTAGE: {percentage:.2f}%
''')
if percentage >= 40:
    print("RESULT:PASS")
else:
    print("RESULT:FAIL")


#METHOD 2

physics = float(input("Enter the marks out of 100 : "))
mathematics = float(input("Enter the marks out of 100 : "))
electronics = float(input("Enter the marks out of 100 : "))

total_marks = physics + mathematics + electronics
percentage = (total_marks / 300) * 100

print(f'''
REPORT CARD
TOTAL MARKS: {total_marks}
PERCENTAGE: {percentage:.2f}%
RESULT: {"PASS" if percentage >= 40 else "FAIL"}
''')

#METHOD 3

physics = float(input("Enter the marks out of 100 : "))
mathematics = float(input("Enter the marks out of 100 : "))
electronics = float(input("Enter the marks out of 100 : "))

total_marks = physics + mathematics + electronics
percentage = (total_marks / 300) * 100

result = "PASS" if percentage >= 40 else "FAIL"

print(f'''
REPORT CARD
TOTAL MARKS: {total_marks}
PERCENTAGE: {percentage:.2f}%
RESULT: {result}
''')