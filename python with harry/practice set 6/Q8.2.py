# Write a function print_details(**kwargs) that prints key-value pairs passed
# as arguments, for example:
# print_details(name="Alice", age=25, city="Delhi")
# # Output:
# # name: Alice
# # age: 25
# # city: Delhi


def details(**kwargs):
    print(kwargs)

    for item in kwargs.keys():
        print(f"{item}: {kwargs[item]}")


details(name="Alice", age=25, city="Delhi")