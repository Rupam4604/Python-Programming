# Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter  than 4 characters.

words = ["python", "rocks", "ai"]

lengths = [n for w in words if (n := len(w))>= 4]

print(lengths)