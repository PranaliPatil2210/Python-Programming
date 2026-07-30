#  keys() - Returns all the keys in the dictionary.
# Returns a dict_keys view object containing all the keys of the dictionary.
print(student.keys()) # dict_keys(['name', 'age'])
#  It doesn't return a list. It returns a special object called: dict_keys
print(type(student.keys())) # <class 'dict_keys'>


# values() - Returns all the values.
# Returns a dict_values view object containing all the values of the dictionary.
print(student.values()) # dict_values(['Pranali', 20])
print(type(student.values())) # <class 'dict_values'>


# items() - It returns each key-value pair as a tuple.
# Returns a dict_items view object.
# Each element inside the dict_items object is a tuple containing one key-value pair.
print(student.items()) # dict_items([('name', 'Pranali'),('age', 20)])
for key, value in student.items(): # Python unpacks the tuple into two variables.
    print(key, value)
    
# View Objects
# dict_keys, dict_values, and dict_items are view objects, not copies.
# They always reflect the latest changes made to the dictionary.
student = {
    "name": "Pranali"
}
k = student.keys()
print(k)

student["age"] = 20
print(k)   