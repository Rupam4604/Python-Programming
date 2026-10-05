# Write a function sum_all(*args) that accepts any number of integers and
# returns their sum.

def sum_all(*args):
    sum = 0
    for item in args:
        sum += item

    return sum

print(sum_all(2, 5, 50, 10))