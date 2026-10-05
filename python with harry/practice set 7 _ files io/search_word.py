# Write a command-line utility search_word.py that takes two arguments:

# A filename
# A word to search and prints how many times the word appears in the file.

import sys

def search_words(words, string):
    return string.count(words)

if __name__ == "__main__":
    filename = sys.argv[1]
    words = sys.argv[2]
    with open(filename) as f:
        string = f.read()
        n = search_words(words,string)
        print(f"there are {n} occurences of '{words}' in the {filename}")

