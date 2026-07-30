# List Comprehension - A list comprehension is a shorter and cleaner way to create a new list using a loop.

squares = [i * i for i in range(1, 6)]
print(squares)

# List Comprehension with if

numbers = [1, 2, 3, 4, 5, 6]

even = [i for i in numbers if i % 2 == 0] 
print(even)