# Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
class negativenumbererror(Exception):
    pass

try:
    a = int(input("enter a number: "))

    if a<0:
        raise negativenumbererror("number can not be nagetive")

    result = 50/a
    print(f"the result is {result}")


except ValueError:
    print("error! please enter a valid number")
except ZeroDivisionError:
    print("error! cannot divided by 0")

except negativenumbererror as e:
    print(f"error! do not enter negative number",e)

