# Subset - A set is a subset if every element exists in another set.
A = {1,2}
B = {1,2,3,4}
print(A.issubset(B))

A <= B

# Superset - Opposite of subset.
A = {1,2,3,4}
B = {1,2}
print(A.issuperset(B))

A >= B

# Disjoint Sets - Two sets are disjoint if they have no common elements.
A = {1,2}
B = {3,4}
print(A.isdisjoint(B))