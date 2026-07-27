def add(*numbers): #One function. Unlimited numbers
    total = 0
    for i in numbers:
        total += i
        
    print("Sum =", total)
    
add(10, 20)
add(10, 20, 30)
add(1, 2, 3, 4, 5)

def numbers(*args):
    print(args)
    
numbers(1,5.83,3,"Panu")
