# Create a text file notes.txt using Python and write "Learning Python is fun!" into it.


f = open("notes.txt", "w")

notes = '''
Learning Python is fun!
'''

f.write(notes)
f.close()