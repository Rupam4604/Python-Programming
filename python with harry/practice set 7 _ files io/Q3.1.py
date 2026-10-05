# Use the os module to:
# Print the current working directory
# List all files and folders in the current directory
# Create a new folder my_folder


import os


print(f"current directory is {os.getcwd()}")  # current working directory
print(os.listdir()) # listing all files in current directory
os.mkdir("my_folder") # creating new folder
