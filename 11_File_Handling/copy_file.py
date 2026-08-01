with open("student.txt", "r") as file:
    data = file.readlines()
    print(data)

with open("student_copy.txt", "w") as file:
    file.writelines(data)