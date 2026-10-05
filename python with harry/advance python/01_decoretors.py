# decorator is a function that takes function, it creats a new function inside its body(wrapper). then it returns that new function 


def decorator(func):
    def wrapper():
        print("i am about to excute a functiuon...")
        func()
        print("i am excuted the function....")
    return wrapper

@decorator   #
def say_hello():
    print("hello!")

say_hello()

# 
#f = decorator(say_hello)
#f()