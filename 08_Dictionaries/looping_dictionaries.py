student = {
    "name": "Pranali",
    "age": 20,
    "branch": "ENTC"
}

# Loop through Keys (Default)
for i in student:
    print(i)

# Using keys()
for key in student.keys(): # This is more explicit and makes the code easier to understand.
    print(key)

# Using values()
for value in student.values():
    print(value)

# Using items()
for key, value in student.items(): # Python automatically unpacks the tuple.
    print(key, value)










