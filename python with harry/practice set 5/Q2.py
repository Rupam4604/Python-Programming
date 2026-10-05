# Constructor and Attributes
# Create a class Person with a constructor ( __init__ ) that accepts name and age
# as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.


class person:
    def __init__(self, name, age):      # creating the constructor (__init__) in class "person"

# instance attribute

        self.name = name    
        self.age = age

# print person method
    def get_info(self):
        print(f"{self.name} is {self.age} years old")


#1    

person1 = person("rupam",22)
print(person1.name, person1.age)



# 2. print person method 

person1.get_info()

