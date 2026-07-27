# for loop
for i in range(5):
    print(i) 
	
# Negative step
for i in range(10,0,-2):
    print(i)

# Iterating over Strings
name = "Python"
for letter in name:
    print(letter)

# Iterating over List
fruits = ["Apple","Banana","Mango"]
for fruit in fruits:
    print(fruit)

# Iterating over Tuple
numbers = (10,20,30)
for i in numbers:
    print(i)

# Iterating over Set
colors = {"Red","Blue","Green"}
for color in colors:
    print(color)
# Order is not guaranteed.

# Iterating over Dictionary (Only keys)
student = {
    "name":"Rahul",
    "age":20,
    "marks":85
}

for key in student:
    print(key)

# Keys and values
for key,value in student.items():
    print(key,value)

# Nested For Loop
for i in range(3):
    for j in range(2):
        print(i,j)

# Factorial
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

for i in range(5):
    print(i)
else:
    print("Loop Completed")





