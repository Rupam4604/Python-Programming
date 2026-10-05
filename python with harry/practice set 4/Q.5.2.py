# Create a dictionary of three friends and their phone numbers. Use:
# keys() to get all names
# values() to get all numbers
# items() to loop over key-value pairs and print them


friends = {"rupam" : 8240459326, "kuchu kuchu" : 7278378608, "rimli" : 9332088736}

print(friends.keys())
print(friends.values())


print(friends.items()) ## 1st method
# 2nd method
for key, Value in friends.items():
    print(key,Value)
    