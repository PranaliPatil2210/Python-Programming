def square(n):
    return n * n
	
print(square(3))

def largest_no(a,b):
    if a > b:
        return f"{a} is greater"
    else:
        return f"{b} is greater"
		
print(largest_no(5,8))

def areaOfRectangle(length,breadth):
    print(f"Area of rectangle is: {length*breadth} units")
	
areaOfRectangle(4,5)

def print_star_pattern():
    for i in range(3):
        print("*****")
		
print_star_pattern()

def print_header():
    print("="*20)
	
def print_footer():
    print("="*20)

print_header()
print("Student Report")
print_footer()

def welcome():
    print("Welcome Home!")
for i in range (1,6):
    welcome()






