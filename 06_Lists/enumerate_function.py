students = ["Pranali", "Shreya", "Mayuri"]
for index, name in enumerate(students):
    print(index, name)
	
students_list = ["Pranali", "Shreya", "Mayuri", "Yogesh", "Sarthak",]
for roll_no, name in enumerate(students_list, start=1):
    print(roll_no, name)
	
cart = ["Milk", "Bread", "Eggs"]
print("Shopping Cart")
for sr_no, item in enumerate(cart, start=1):
    print(sr_no, item)