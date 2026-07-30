student = {
    "name": "Pranali",
    "age": 20
}
student["branch"] = "ENTC" # New key → Added
student["age"] = 21 # Existing key → Updated

# update() Method
student.update({
    "age": 22,
    "branch": "CSE"
})

print(student)