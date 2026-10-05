# Write a decorator logger that prints "Function is being called" before
# the function runs. Use it to decorate a function say_hello() that prints
# # "Hello!" .



def looger(func):
    def wrapper():
        print("the function is being called")
        func()
    return wrapper

@looger
def say_hello():
    print("hello!")

say_hello()