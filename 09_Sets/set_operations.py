# Python Set Operations

# Union - Union means combine all unique elements from both sets.
# | Operator
A = {1,2,3,4}
B = {3,4,5,6}
print(A | B)

# union()
print(A.union(B))

# Intersection - Intersection means common elements in both sets.
# &
A = {1,2,3,4}
B = {3,4,5,6}
print(A & B)

# intersection()
print(A.intersection(B))

# Difference - Difference means elements present in the first set but not in the second.
A = {1,2,3,4}
B = {3,4,5,6}
print(A - B) # {1,2}
print(B - A) # {5,6} 
# Difference is not commutative. A - B ≠ B - A

# difference()
print(A.difference(B))

# Symmetric Difference - Elements present in either set but not in both.
A = {1,2,3,4}
B = {3,4,5,6}
print(A ^ B) # {1,2,5,6} Union − Intersection

print(A.symmetric_difference(B))