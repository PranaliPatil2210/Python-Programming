students = (
    ("Pranali", "ENTC", 8.54),
    ("Sonali", "CSE", 8.00),
    ("Manali", "Mech", 9.57),
    ("Vrushali", "Chem", 7.54),
    ("Chaitrali", "Electrical", 8.54)
)

# 1. Print all student details
print("Student Details:")
for name, branch, cgpa in students:
    print(f"Name   : {name}")
    print(f"Branch : {branch}")
    print(f"CGPA   : {cgpa}")
    print()

# 2. Print total number of students
print("Total Students:", len(students))

# 3. Check whether 'Pranali' is present
found = False
for name, branch, cgpa in students:
    if name == "Pranali":
        found = True
        break

print("Is Pranali Present?", found)

# 4. Print student at index 2
print("Student at Index 2:", students[2])