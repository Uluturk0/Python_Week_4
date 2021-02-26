'''
Developer: Ömer ULUTÜRK
Date: 24.02.2021
Purpose of Software: Reinforcement of learned Python Code and Self-improvement


As a user, I want to use a program which can calculate basic mathematical operations.
So that I can add, subtract, multiply or divide my inputs.

Acceptance Criteria:

The calculator must support the Addition, Subtraction, Multiplication and Division operations.
Define four functions in four files for each of them, with two float numbers as parameters.
To calculate the answer, use math.ceil() and get the next integer value greater than the result
Create a menu using the print command with the respective options and take an input choice from the user.
Using if/elif statements for cases and call the appropriate functions. Use try/except blocks to verify
input entries and warn the user for incorrect inputs. Ask user if calculate numbers again.
To implement this, take the input from user Y or N.
'''

import math
# This function adds two numbers
def add(x, y):
    return math.ceil(x + y)

# This function subtracts two numbers
def subtract(x, y):
    return math.ceil(x - y)

# This function multiplies two numbers
def multiply(x, y):
    return math.ceil(x * y)

# This function divides two numbers
def divide(x, y):
    return math.ceil(x / y)


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid Input")

    answer = input("Press any key to continue and 'Q' to exit.")
    if answer=="q" or answer=="Q":
        print("Thank you for using the application.")
        break