Student Record System
while True:

    print("""
1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Exit
""")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            name = input("Enter student name: ")

            with open("students.txt", "a") as file:
                file.write(name + "\n")

        case 2:

            with open("students.txt", "r") as file:
                print(file.read())

        case 3:

            name = input("Enter student name: ")

            with open("students.txt", "r") as file:
                data = file.read()

            if name in data:
                print("Student Found")
            else:
                print("Student Not Found")

        case 4:

            name = input("Enter student name: ")

            with open("students.txt", "r") as file:
                lines = file.readlines()

            with open("students.txt", "w") as file:
                for line in lines:
                    if line.strip() != name:
                        file.write(line)

            print("Record Deleted")

        case 5:
            print("Exiting...")
            break

        case _:
            print("Invalid Choice")