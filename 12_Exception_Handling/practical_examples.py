# 1. File handling + exception handling

try:
    with open("student.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File does not exist.")
	
	
# 2. Function + exception handling

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")
	

# 3. Marks validator	

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

except ValueError as e:
    print("Invalid marks:", e)

else:
    print("Marks accepted:", marks)

finally:
    print("Validation completed.")
	

# 4. Student marks / input validation

try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 to 100")
except ValueError as e:
    print("Invalid ", e)
else:
    print("Your marks are ", marks)
finally:
    print("Done")
	

	
