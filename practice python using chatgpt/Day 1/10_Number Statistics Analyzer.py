# Number Statistics Analyzer.

# Ask the user to enter 10 numbers, one by one.

# Your program must calculate:

# Total/sum
# Average
# Largest number
# Smallest number
# Number of even numbers
# Number of odd numbers
# Number of positive numbers
# Number of negative numbers
# Number of zeros

i = 1
total = 0
even_count = 0
odd_count = 0
postive_count = 0
negative_count = 0
zero_count = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))     # asking user input

# Initial value  @ First number → current_large  @First number → current_small
    if i == 1:                                  
        large_num = num
        small_num = num
    total = total + num
# largest number checking
    if num > large_num:
        large_num = num
    else:
        large_num = large_num
# Smallest number checking
    if num < small_num:
        small_num = num
    else:
        small_num = small_num
# Even & odd number checking and counting 
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
# positive \ negative \ zero checking and counting
    if num > 0:
        postive_count = postive_count + 1
    elif num == 0:
        zero_count = zero_count + 1
    else:
        negative_count = negative_count + 1


average = total / 10

result = f'''
Total: {total}
Average: {average}
Largest number: {large_num}
Smallest number: {small_num}
Number of even numbers: {even_count}
Number of odd numbers: {odd_count}
Number of positive numbers: {postive_count}
Number of negative numbers: {negative_count}
Number of zeros: {zero_count}
'''
print(result)