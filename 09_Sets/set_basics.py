# Set - A set is an unordered collection of unique elements.

# Characteristics of Sets
# Unordered
# No indexing
# No slicing
# Mutable
# Duplicates are removed automatically.

# Creating Sets
s = {1,2,3}
s = set([1,2,3])

# Empty Set
s1 = {} # {} creates an empty dictionary.
print(type(s1))  # <class 'set'>

s2 = set()
print(type(s2))  # <class 'set'>

# Checking Membership
s = {10,20,30}
print(20 in s)
print(50 in s)

# Length
print(len(s))

list1 = [10,20,30,20,10]
print(set(list1))







