# Open tasks.txt in append mode and add a new line "Task Completed!".



f = open("tasks.txt", "a")

add = '''
Har Har Mahadev
Task Completed
'''

f.write(add)

f.close()