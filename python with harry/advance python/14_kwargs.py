def marks(**kwargs):
    print(kwargs)

# kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"the marks of {item} is {kwargs[item]}")   


marks(rupam=22, rimli=10, soumyadipta=24, malkin= 48)