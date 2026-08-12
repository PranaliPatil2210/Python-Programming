# Mini Project 1 — Calculator

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = int(input("1. Add 2.Sub 3.Mul 4. Div Enter the operation no: "))
    if operator == 1:
        print("Addition is: ", a + b)
    elif operator == 2:
        print("Subtraction is: ", a - b)
    elif operator == 3:
        print("Multiplication is: ", a * b)
    elif operator == 4:
        print("Division is: ", a / b)
    else:
        print("Invalid Operator")

except ZeroDivisionError:
    print("Dividion by zero is not allowed")

except ValueError as e:
    print("Error ", e)


# Mini Project 2 — ATM

try: 
    balance = 5000
    option = int(input("1. Deposit 2. Withdraw 3. Check Balance \n Enter your option: "))
    if option < 0 or option > 3:
    # if option not in [1, 2, 3]:
        raise ValueError("Enter valid option")
    match option:
        case 1:
            deposit = int(input("Enter the amount you want to deposite: "))
            if deposit <= 0:
                raise ValueError("Deposite can not be negative or zero")
            else:
                balance = balance + deposit
        case 2:
            withdrawal = int(input("Enter the amount you want to withdraw: "))
            if withdrawal < 0:
                raise ValueError("Withdrawal can not be negative ")
            if withdrawal > balance:
                raise ValueError("Withdrawal can not be greater than balance")
            else:
                balance = balance - withdrawal
        case 3:
            print("Your balance is: ", balance)
        
        
except ValueError as e:
    print("Error", e)

finally:
    print("Transaction Completed")
