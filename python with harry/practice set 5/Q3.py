# Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().


class animal:
    def sound(self):
        print("some sound")

class dog:
    def sound(self):
        print("bark")

a = animal()
a.sound()

b = dog()
b.sound()