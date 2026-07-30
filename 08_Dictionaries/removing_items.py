# del
student = {
    "name": "Pranali",
    "age": 20
}
del student["age"]
print(student)

# Uncomment to see KeyError
# If the key doesn't exist:
# del student["city"] # KeyError

del student # the variable itself is deleted.

# pop() - Removes the key and returns its value.
student = {
    "name": "Pranali",
    "age": 20
}
age = student.pop("age")
print(age)
print(student)
# dictionary.pop(key, default_value)
student = {
    "name": "Pranali"
}
print(student.pop("age", "Not Found"))

# popitem() - Removes the last inserted item.
student = {
    "name": "Pranali",
    "age": 20,
    "branch": "ENTC"
}
student.popitem() # In Python 3.7+, popitem() follows insertion order.
print(student)

# clear() - Deletes all items.
student = {
    "name": "Pranali",
    "age": 20
}
student.clear() # The dictionary still exists. It's just empty.
print(student)















