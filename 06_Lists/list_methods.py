students = ["Pranali", "Shreya", "Mayuri"]

# append() - adds one element to the end of the list.
students.append("Yogesh")
print(students)

# insert() - inserts an element at a specific position.
students.insert(0, "Aniket")
print(students)

# extend() - adds all elements of another iterable to the end of the current list.
students.extend(["Riya", "Karan"])
print(students)

# remove() - remove() removes the first occurrence of a specified value from the list
students.remove("Mayuri")
print(students)

students.append("Yogesh")
print(students)

students.remove("Yogesh")
print(students)

# pop() - removes an element using its index and returns the removed element.
x = students.pop()
print("Transferrred Student: ", x)

# count() - returns how many times a value appears in the list.
print(students.count("Yogesh"))

# index() - returns the index of the first occurrence of a specified value.
print(students.index("Shreya"))

# sort() - arranges the list in ascending order by default.
students.sort()
print(students)

# reverse() - reverses the current order of the list.
students.reverse()
print(students)

# copy() - creates a shallow copy of a list.
new_students = students.copy()
print(new_students)

new_students.append("Om")
print("Original List:", students)
print("Copied List:", new_students)