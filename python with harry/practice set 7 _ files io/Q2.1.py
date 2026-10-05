# Write a program that writes three lines of text to a file tasks.txt.



f = open("tasks.txt", "w")

task = '''
hello 
good morning
Ganpati Bappa Morya!
'''

f.write(task)
f.close()