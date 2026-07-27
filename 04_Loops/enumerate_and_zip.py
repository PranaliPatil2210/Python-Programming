# enumerate()
fruits = ["Apple","Banana","Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# zip() - Loop over multiple sequences together.
names = ["A","B","C"]
marks = [80,90,70]
for name, mark in zip(names, marks):
    print(name, mark)







