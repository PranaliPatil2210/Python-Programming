# Nested Dictionaries
students = {
    101: {
        "name": "Pranali",
        "age": 20,
        "branch": "ENTC"
    },

    102: {
        "name": "Rahul",
        "age": 21,
        "branch": "CSE"
    }
}

# Accessing Data
students[101]
print(students[101]["name"])
print(students[102]["branch"])

# Updating Nested Dictionary
students[101]["age"] = 21
print(students[101])

# Adding New Data
students[101]["cgpa"] = 8.54

# Looping Through Nested Dictionary
for roll, info in students.items(): 
    print(roll, info)

for roll, info in students.items():
    print(roll, info["name"], info["age"])

