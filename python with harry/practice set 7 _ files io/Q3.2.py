# Use the shutil module to:
# Copy a file from one folder to another
# Move a file to a new folder
# Delete a file (careful: irreversible!)

import shutil

shutil.copy("tasks.txt", "new.txt")  # Copy a file from one folder to another

shutil.move("tasks.txt", "my_folder")   # Move a file to a new folder

shutil.rmtree()  # Deleting a file (careful: irreversible!)
