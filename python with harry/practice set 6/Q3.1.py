# Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b .
# A @classmethod called description(cls) that prints "This is a
# utility class for math operations."
# Call both methods without creating an object.





class mathutlis:
    def __init__(self):
        pass

    @staticmethod
    def add(a,b):
        return a+b

    @classmethod
    def description(cls):
        print("thyis is a utility class for math operatioins")

# creating an object
'''
a = mathutlis
print(a.add(5,6))
a.description()

'''

# without creating an object

print(mathutlis.add(50, 10))
mathutlis.description()