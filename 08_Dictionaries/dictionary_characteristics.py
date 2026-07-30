# Keys Must Be Unique
student = {
    "name": "Pranali",
    "name": "Aditi"
}
print(student) 

# Values Can Be Duplicated
student = {
    "student1": "Pranali"
    "student2": "Pranali"
}
print(student)

# Mutable 
# Ordered
d = {
    "A": 1,
    "B": 2,
    "C": 3
}
print(d)

# Valid keys:
d = {
    1: "Integer",
    3.14: "Float",
    True: "Boolean",
    "name": "String",
    (1, 2): "Tuple"
}
# Lists are mutable, so they cannot be used as dictionary keys.
