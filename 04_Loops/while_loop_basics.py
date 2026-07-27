# WHILE LOOP
count=1
while count <= 5:
    print(count)
    count+=1

# Sum of Numbers
i = 1
sum2=0
limit= int(input("Enter no. you want sum upto (1 to 100): "))
while i<=100:
    sum2+=i
    if i==limit:
        break
    i+=1
print(f"sum of 1 to {limit} numbers is {sum2}")


# Factorial
i=5
fact=1
while i > 0:
    fact *= i
    i -= 1






