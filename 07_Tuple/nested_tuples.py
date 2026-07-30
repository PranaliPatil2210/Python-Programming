# Nested Tuples 
students = (
    ("Pranali", 20),
    ("Shreya", 21),
    ("Mayuri", 20)
)
print(students)
print(students[0][0]) # Accessing Elements
print(students[1][1])
for name, age in students:  # Looping Through Nested Tuples
    print(name, age)
	
data = (10, [20, 30], 40)
data[1].append(50)
print(data)