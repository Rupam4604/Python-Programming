class Animal:  # Parent class (superclass)
    location = "india"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("generic animal sound")


class dog(Animal):
    def speak(self):
        print("woof!")


a = Animal("dog")
a.speak()

d = dog("bruno")
d.speak()
print(d.location)