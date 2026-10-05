# Write a program that merges two dictionaries into one

dict1 = {"a" : 5, "b" : 8, "c" : 10}
dict2 = {"d" : 9, "e" : 15, "f" : 50}

dict1.update(dict2)
print(dict1)

# 2nd solution

def merged_dict(d1, d2):
    return{**d1, **d2}

di_1 =  {"a" : 5, "b" : 8, "c" : 10}
di_2 = {"d" : 9, "e" : 15, "f" : 50}

merged = merged_dict(di_1, di_2)
print(merged)