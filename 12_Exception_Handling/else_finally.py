# The else Block
# else runs only when the try block completes successfully without an exception.
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)


# The finally Block
# finally is special. It executes whether an exception occurs or not.

try:
    number = 10 / 2

except ZeroDivisionError:
    print("Error")

finally:
    print("Program finished")


try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
finally:
    print("Done")
	
try:
    number = 10 / 0

except ZeroDivisionError:
    print("Error")

finally:
    print("Program finished")

