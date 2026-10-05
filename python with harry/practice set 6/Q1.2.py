# Write a decorator timer that calculates how long a function takes to execute.
# Test it with a function that sums numbers from 1 to 1,000,000.
from time import time
def timer(func):
    def wrapper(n):
        t1 = time()
        result = func(n)
        t2 = time()
        print("calculating how long a function takes to excute: ",t2 - t1)
        return result
    return wrapper

@timer
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

a = sum(1000000)
print(a)
