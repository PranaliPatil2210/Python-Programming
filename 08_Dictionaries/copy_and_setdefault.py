# copy()
student = {
    "name":"Pranali",
    "age":20
}

student2 = student.copy() #It creates a shallow copy.

student = {
    "name":"Pranali"
}
student.setdefault("name","Rahul") # Key Exists
print(student) # {'name':'Pranali'}

# Key Doesn't Exist
# setdefault()
student = {
    "name":"Pranali"
}
student.setdefault("age",20) # Python adds the key.
print(student





