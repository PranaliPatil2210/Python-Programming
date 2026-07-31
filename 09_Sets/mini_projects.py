# Student Club Manager

students = {
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", 
    "Sai", "Reyansh", "Aanya", "Diya", "Ananya", 
    "Pari", "Siya", "Shanaya", "Avni", "Ishaan"
}
club1 = {"Sai", "Reyansh", "Aanya", "Diya", "Ananya"}
club2 = {"Vihaan", "Arjun", "Shanaya", "Avni", "Sai", "Reyansh", "Aanya"}
print('''Menu :\n 1. Add\n2. Remove\n3. Display\n4. Union\n5. Intersection\n6. Difference\n7. Membership\n8.Exit''')
num = int(input("Enter a number for operation: "))
student = input("Enter student name : ")
match(num):
    case 1:
        students.add(student)
        print(students)
    case 2:
        students.remove(student)
        print(students)
    case 3:
        print(students)
    case 4:
        print(club1 | club2)
    case 5:
        print(club1 & club2)
    case 6:
        print(club1 ^ club2)
    case 7:
        print(student in students)
    case 8:
        print("Exiting...")
    case default:
        print("Invalid Input")


# Menu Driven Set Operations

event1 = {"user1", "user2", "user3", "user4","user5"}
event2 = {"user3","user4","user7","user8","user9"}
print('''Menu :\n 1. Add\n2. Remove\n3. Display\n4. Union\n5. Intersection\n6. Difference\n7. Exit''')
num = int(input("Enter a number for operation: "))
match(num):
    case 1:
        event1.add("user6")
        print(event1)
    case 2:
        event2.remove("user8")
        print(event2)
    case 3:
        print(event1)
        print(event2)
    case 4:
        print(event1 | event2)
    case 5:
        print(event1 & event2)
    case 6:
        print(event1 - event2)
        print(event2 - event1)
    case 7:
        print("Exiting...")
    case default:
        print("Invalid Input")

