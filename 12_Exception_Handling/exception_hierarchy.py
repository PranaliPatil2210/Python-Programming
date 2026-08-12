# Exception Hierarchy 
BaseException
│
└── Exception
    │
    ├── ValueError
    ├── TypeError
    ├── KeyError
    ├── IndexError
    ├── FileNotFoundError
    └── ZeroDivisionError

try:
    ...
except Exception:
    print("Something went wrong")

# Exception is a broad category for many ordinary runtime exceptions.

# Bare except
except:
# This catches very broadly.

# Exception Propagation

def divide(a, b):
    return a / b


def calculate():
    return divide(10, 0)


try:
    calculate()

except ZeroDivisionError:
    print("Division error")

calculate()
    ↓
divide()
    ↓
10 / 0
    ↓
ZeroDivisionError
    ↓
exception propagates outward
    ↓
matching except found

# Nested try-except

try:

    try:
        number = int(input("Enter number: "))
        print(10 / number)

    except ValueError:
        print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
 