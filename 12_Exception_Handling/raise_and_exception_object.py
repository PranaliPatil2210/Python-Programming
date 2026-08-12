# raise
# Python normally raises exceptions automatically.
# But you can deliberately raise one.

age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
	
# ValueError: Age cannot be negative

marks = 150
if marks > 100:
    raise ValueError("Marks cannot exceed 100")
	
# raise with try-except
# You can raise an exception and catch it.
try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative")

except ValueError as e:
    print("Error:", e)

# Exception Object — as

try:
    number = int("hello")

except ValueError as e:
    print(e)

# Here:
# as e - stores the exception object in e.
# So e contains information about what went wrong.

except ValueError as error:
    print("Something went wrong:", error)
# The variable name doesn't have to be e.