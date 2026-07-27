# brreak
for i in range (1, 101, 1):
    print(i, end=" ")
    if (i == 50):
        break
    else:
        print("I am Pranali")
print("Thank you")


for i in range (12):
    if (i==10):
        break
    print(5 * (i+1))


correct_password = "python123"
while True:
    password = input("Password: ")
    if password == correct_password:
        print("Access Granted")
        break
    print("Wrong Password")


# continue 
# Ignore invalid marks
marks = [75, -1, 84, 91]
for mark in marks:
    if mark < 0:
        continue
    print(mark)


# Skip empty strings
names = ["Raj", "", "Amit", "", "Riya"]
for name in names:
    if name == "":
        continue
    print(name)

# pass
for i in range(5):
    pass
	
while True:
    pass





