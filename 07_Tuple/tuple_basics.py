tuple1 = (10, 20, 30) # Creating Tuple
tuple2 = 10, 20, 30 # You can also create a tuple without parentheses.

# Ordered Collection
# Immutable
student = ("Pranali", 20, "ENTC", 8.54, True, 20) # Tuple Allows Duplicate Values
print(student)

# Indexing 
student = ("Pranali", 20, "ENTC", 8.54)
print(student[0])
print(student[1])
print(student[-1])
print(student[-2])

# Tuple Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])

# Single-Element Tuple
t2 = (5,)
print(type(t2))

# Tuple Methods

# count() - Counts how many times a value appears.
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# index() - Returns the index of the first occurrence.
fruits = ("Apple", "Mango", "Banana", "Mango")
print(fruits.index("Mango"))
print(fruits.index("Orange")) # If the value is not present: ValueError

# Membership Operators
fruits = ("Apple", "Mango", "Banana")
print("Apple" in fruits)
print("Orange" not in fruits)

