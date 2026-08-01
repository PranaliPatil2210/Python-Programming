# read() - reads the entire file and returns it as a single string.
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# Read specific number of characters
data = file.read(7) # Pranali
# Only the first 7 characters are read.

# readline() - Reads only one line at a time.
line = file.readline()
# Calling it again:
line = file.readline()
# Every call moves to the next line.

# readlines() - Reads all lines and stores them in a list.
lines = file.readlines() # ['Pranali\n', 'Mayuri\n', 'Aishwarya\n', 'Rahul\n']
# Notice the \n (newline character) at the end of each line.

# Reading Using a Loop 
# Instead of using readlines(), we usually iterate over the file.
for line in file:
    print(line)