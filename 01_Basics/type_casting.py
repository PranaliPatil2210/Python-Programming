"""
Topic: Type Casting in Python

Description:
This program demonstrates explicit and implicit type casting in Python.

Author: Pranali Patil
"""

# -------------------------
# Explicit Type Casting
# -------------------------

a = "2"
b = "4"

print("Explicit Type Casting:")
print(int(a) + int(b))
print(a + b)

name = "10"
date = "22"

print(float(name) + float(date))

num1 = 10.5
num2 = 11.8

print(int(num1) + int(num2))


# -------------------------
# Implicit Type Casting
# -------------------------

c = 1.8
d = 5

print("\nImplicit Type Casting:")
print(c + d)
print(type(c + d))