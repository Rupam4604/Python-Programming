# Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:

# python count_lines.py tasks.txt
# # Output: Number of lines: 4

import sys

def count_lines(file_name):
    with open(file_name) as f:
        return len(f.readlines())

if __name__ == "__main__":
    file_name = sys.argv[1]
    num_lines = count_lines(file_name)
    print(f"there are {num_lines} lines in {file_name}")



