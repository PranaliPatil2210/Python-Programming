# write() - writes a string to a file.
# Syntax:
# file.write("Hello")
# If the file is opened in:
# w mode → Existing content is erased first.
# a mode → Data is added at the end.

# Multiple write()
file.write("Python\n")
file.write("C\n")

# writelines() - Writes multiple strings at once.
# Syntax - file.writelines(list_of_strings)
students = [
#     "Pranali\n",
#     "Mayuri\n",
#     "Aishwarya\n"
# ]
file.writelines(students)

# Append Mode (a)
file = open("sample.txt","a")

# Example

list1 = ["Pranali - 95\n", "Mayuri - 90\n", "Rahul - 88"]
with open("marks.txt","w") as file:
    file.writelines(list1)

with open("marks.txt", "a") as file:
    file.write("\nSai - 91")