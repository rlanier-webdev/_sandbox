# Simple Calculator
# Use a dictionary to simplify a long if statement

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


while True:
    # user input
    choice = {
        "1", add(num1, num2),
        "2", subtract(num1, num2),
        "3", multiply(num1, num2),
        "4", divide(num1, num2)
    }
    
    choice = [1,2,3,4]
    
    action = input(f"Enter {choice}: ")
    
    operation = choice.get(action)
    
    if operation:
        operation(choice)
    else:
        print("Action not recognized")
    
    # check against user input
    # if choice in ('1','2','3','4'):
    #     num1 = float(input("Enter first number: "))
    #     num2 = float(input("Enter second number: "))
        
    #     if choice == '1':
    #         print(num1, "+", num2, "=", add(num1, num2))
    #     elif choice == '2':
    #         print(num1, "-", num2, "=", subtract(num1, num2))
    #     elif choice == '3':
    #         print(num1, "*", num2, "=", multiply(num1, num2))
    #     elif choice == '4':
    #         print(num1, "/", num2, "=", divide(num1, num2))
        
    #     # check to see if user wants another calculation
    #     # if no break the loop
    #     next_calc = input("Another calculation? (yes/no): ")
        
    #     if next_calc == "no":
    #         break
    
    # else:
    #     print("Invalid Input")