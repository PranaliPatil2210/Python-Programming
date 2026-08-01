# Count Lines, Words and Characters

with open("student.txt", "r") as file:
    data = file.read()

characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)


# Find the Longest Line

with open("student.txt", "r") as file:
    lines = file.readlines()

longest = max(lines, key=len) # Doesn't compare the strings themselves. Compares their lengths.

print("Longest Line:")
print(longest.strip()) #strip() removes \n, leading spaces & trailing spaces.

# Find the Shortest Line

with open("student.txt", "r") as file:
    lines = file.readlines()

shortest = min(lines, key=len)

print("Shortest Line:")
print(shortest.strip())


# Count Occurrences of a Word
word = input("Enter word: ")

with open("student.txt", "r") as file:
    data = file.read()

print("Occurrences:", data.count(word))


# Convert File to Uppercase

with open("student.txt", "r") as file:
    data = file.read()

with open("uppercase.txt", "w") as file:
    file.write(data.upper())

print("Uppercase file created successfully.")


# Reverse File Contents
with open("student.txt", "r") as file:
    data = file.read()

with open("reverse.txt", "w") as file:
    file.write(data[::-1])

print("Reverse file created successfully.")


# Merge Two Files

with open("student.txt", "r") as file1:
    data1 = file1.read()

with open("marks.txt", "r") as file2:
    data2 = file2.read()

with open("merged.txt", "w") as file3:
    file3.write(data1)
    file3.write("\n")
    file3.write(data2)

print("Files merged successfully.")
