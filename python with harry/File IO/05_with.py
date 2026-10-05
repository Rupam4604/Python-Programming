# f = open("rupam.txt", "r")
# content = f.read()
# print(content)
# f.close()

# No need to write f.close() beacuse file is automaticaly closed by default when using  "with" syntex

with open("rupam.txt","r") as f:  # context manager
    content = f.read()
    print(content)