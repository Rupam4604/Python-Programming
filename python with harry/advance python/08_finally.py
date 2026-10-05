
def divide(a, b):
    try:
        c= a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

# this is always excuted no matter if try completely excute or nor 
    finally:
        print("this is always excuted")


a= int(input("enter the number 1: "))
b= int(input("enter the number 2: "))
divide(a,b)