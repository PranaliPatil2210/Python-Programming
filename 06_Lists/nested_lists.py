# Accessing Elements
students = [
    ["Pranali", 20],
    ["Shreya", 21],
    ["Mayuri", 20]
]
print(students[0][0])

# Modifying Nested Lists
students[0][1] = 22 
print(students)

# Access Individual Values - This is called unpacking while looping.
students = [
    ["Pranali", 20],
    ["Shreya", 21],
    ["Mayuri", 20]
]

for name, age in students:
    print(name, age)
	
students = [
    ["Pranali", "ENTC", 8.54],
    ["Sonali", "CSE", 8.00],
    ["Manali", "Mech", 9.57],
    ["Vrushali", "Chem", 7.54],
    ["Chaitrali", "Electrical", 8.54],

]

for name, branch, cgpa in students:
    print(f"Name : {name}\nBranch : {branch}\nCGPA : {cgpa}\n")