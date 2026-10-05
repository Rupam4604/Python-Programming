# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else :
#         return False



a = [1, 13, 5, 50, 75, 147, 54, 60, 2, 30, 5, 10, 8, 100]

new = list(filter(lambda x: x>9 , a))

# new = list(filter(is_greater_than_9, a))
print(new)