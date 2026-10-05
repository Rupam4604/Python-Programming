numbers = [1, 2, 5, 45, 85, 5, 58, 60]

# def squre(x):
#     return x*x

# new = list(map(squre, numbers))


new = list(map(lambda x: x*x , numbers))

print(new)