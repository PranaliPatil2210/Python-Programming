# The try Block
# The try block contains code that might produce an exception.
# Syntax:
try:
    # code that may cause an exception
# But try must be followed by an exception handler such as except.

# The except Block
# If this particular exception occurs, execute this code instead of crashing immediately.
# Example:

try:
    result = 10 / 0
	
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    number = int(input("Enter number: "))

except ValueError:
    print("Please enter a valid integer.")
	
	
# Important Built-in Exceptions
# 1 ValueError - Occurs when a function receives the correct general type but an inappropriate value.
number = int("hello")
# Python can't convert "hello" into an integer. So:
ValueError

# 2 TypeError - Occurs when an operation/function is used with an inappropriate type.
result = "10" + 5  # You can't directly add a string and integer.
TypeError

len(10) # An integer doesn't have a length.
TypeError

# 3 ZeroDivisionError
10 / 0
10 // 0
ZeroDivisionError

# 4 IndexError - Occurs when you access an invalid sequence index.
numbers = [10, 20, 30]
print(numbers[5])
# Valid indexes:
# 0
# 1
# 2
# Index 5 doesn't exist.
IndexError

# 11.5 KeyError - Occurs when accessing a dictionary key that doesn't exist.
student = {
    "name": "Pranali",
    "marks": 90
}
print(student["age"]) # There is no "age" key.
KeyError

# 6 NameError - Occurs when Python can't find the variable/function name you're trying to use.
# print(age) # if age was never defined.
NameError

# 7 FileNotFoundError - You've already studied file handling, so this one is especially relevant.
with open("student.txt", "r") as file:
    data = file.read()
# If student.txt doesn't exist:
FileNotFoundError

# 8 AttributeError - Occurs when an object doesn't have the attribute/method you're trying to access.
numbers = [1, 2, 3]
numbers.upper() # Lists don't have an .upper() method.
AttributeError

try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

