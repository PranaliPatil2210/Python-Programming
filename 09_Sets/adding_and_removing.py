# Adding Elements
# add() - Adds one element.
s1 = {10,20}
s1.add(30)
print(s1)

# update() - Adds multiple elements.
s2 = {10,20}
s2.update([30,40])
s2.update((50,60))
print(s2)

# Removing Elements
# remove() - Removes element.
s3 = {10,20,30}
s3.remove(20)
print(s3)
s3.remove(100) # KeyError

# discard() - Same as remove but no error. Gives the set again
s4 = {10,20}
s4.discard(100)
print(s4)

# pop() - Removes a random element.
s5 = {10,20,30}
print(s5.pop())
print(s5)

# clear() - Removes everything.
s6 = {1,2,3}
s6.clear()
print(s6) # set()

# copy()
s7 = {1,2,3}
s8 = s1.copy()
print(s8)
