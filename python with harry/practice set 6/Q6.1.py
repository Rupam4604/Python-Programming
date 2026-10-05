# Use map() to convert [1, 2, 3, 4, 5] into their cubes.
# Use filter() to get only even numbers from [10, 11, 12, 13, 14] .
# Use reduce() from functools to find the product of all elements in [1, 2,
# 3, 4] .


cube = [1, 2, 3, 4, 5]

print(list(map(lambda x: x*x*x, cube)))


even = [10, 11, 12, 13, 14]

print(list(filter(lambda x: x%2 ==0 , even )))

from functools import reduce
product = [1, 2, 3, 4]

print(reduce(lambda x,y : x+y,product))