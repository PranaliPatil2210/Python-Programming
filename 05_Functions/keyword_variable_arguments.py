def display_student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_student_details(name="Pranali", age=20, branch="ENTC")