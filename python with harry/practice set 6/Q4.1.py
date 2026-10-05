# Create a class Book with attributes title and author .
# Implement __str__() so that printing the object displays "Title by
# Author" .
# Implement __len__() so that len(book) returns the length of the title.
# Create two Book objects and test these methods.

class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"the book {self.title} is author by {self.author}"

    def __len__(self):
        return len(self.title)


b1 = book("python programming", "harry")
b2 = book("vlsi","iit kgp")

print(b1)
print(len(b1))
print(b2)
print(len(b2))