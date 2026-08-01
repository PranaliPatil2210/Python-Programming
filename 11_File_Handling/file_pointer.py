# File Pointer

# Whenever a file is opened, Python maintains a file pointer (cursor).
tell() - tells the current position of the file pointer.

with open("sample.txt", "r") as file:
    print(file.tell()) # Output 0

# After reading
# file.read(5)
# print(file.tell()) # Output 5


# 4. seek() - seek() moves the file pointer to a specified position.
# Syntax
# file.seek(position)

# Suppose file contains
# Python Programming
file.read(6)
# Pointer
# Python Programming
#       ^
file.seek(0)
# Pointer returns to
# Python Programming
# ^
# Reading again
print(file.read(6)) # Output Python

