# Python File Handling - File Handling is the process of creating, opening, reading, writing, updating, and deleting files using Python.
# A file is used to store data permanently. 
# Unlike variables, which lose their values when the program ends, data stored in a file remains available until it is changed or deleted.

#  Opening a File - Python uses the built-in open() function.
# Syntax: file = open("filename", "mode")
file = open("student.txt", "r")
# "student.txt" → File name
# "r" → Mode (Read)

# 1. Read Mode (r) - Opens an existing file.
# Cannot modify the file.
# Gives an error if the file doesn't exist.
file = open("student.txt", "r")
# 2. Write Mode (w) - Creates the file if it doesn't exist.
# If the file already exists, all previous content is erased.
file = open("student.txt", "w")
# 3. Append Mode (a) - Adds data to the end of the file.
# Existing data remains unchanged.
# 4. Exclusive Create (x) - Creates a new file.
# If the file already exists: FileExistsError

# Closing a File
# After using a file:
file.close()
# This releases the file resources.


# with open("student.txt", "r") as file:
#     # work with file
# When the with block ends, Python automatically closes the file, even if an error occurs.

# with open()
with open("student.txt","r") as file:
    data = file.read()
    print(data)

# With with:
# File closes automatically.
# Cleaner code.
# Safer.
# Preferred in real-world projects.