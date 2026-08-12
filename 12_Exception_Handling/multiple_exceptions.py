# Multiple except blocks
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# How Python Chooses an except
# Python doesn't execute all except blocks.
# try
#  ↓
# exception occurs
#  ↓
# What exception?
#  ↓
# Find matching except
#  ↓
# Execute it

# Multiple Exceptions in One except
# If the same handling should apply to multiple exceptions:
try:
    ...
except (ValueError, TypeError):
    print("Invalid input")

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = int(input("1. Add 2.Sub 3.Mul 4. Div Enter the operation no: "))
    if operator == 1:
        print("Addition is: ", a + b)
    elif operator == 2:
        print("Subtraction is: ", a - b)
    elif operator == 3:
        print("Multiplication is: ", a * b)
    elif operator == 4:
        print("Division is: ", a / b)
    else:
        print("Invalid Operator")

except ZeroDivisionError:
    print("Dividion by zero is not allowed")

except ValueError as e:
    print("Error ", e)
    