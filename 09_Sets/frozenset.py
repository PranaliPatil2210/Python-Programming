# Frozen Set - A frozenset is an immutable version of a set. 
# You cannot add or remove elements after creation.
fs = frozenset([1,2,3])
print(fs) # frozenset({1,2,3})
fs.add(4) # AttributeError
