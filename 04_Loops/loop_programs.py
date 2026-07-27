# Calculate the sum of the first n natural numbers.
n=int(input("enter a no.: "))
sum5=0
i=1
while i<=n:
    sum5+=i
    i+=1
print(f"sume is {sum5}")

# Find the factorial of a number.
fact=1
i = int(input("Enter a no. for factorial: "))
while i > 0:
    fact*=i
    i-=1
print(fact)

# Reverse the digits of a number
num = 1234
reversednum=0
while num > 0 :
    digit = num % 10
    reversednum = reversednum*10 + digit
    num = num // 10
print(reversednum)

# Count digits
num= 4552
count=0
while num>0:
    count+=1
    num=num//10
print(count)

num5 = map(int, input("Enter 5 numbers: ").split())

for n in num5:
    if n < 0:
        continue
    print(n)

