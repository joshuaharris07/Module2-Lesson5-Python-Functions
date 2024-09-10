# The Calculator App
# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

operation = input("What operation would you like to perform? Add, subtract, multiply, or divide? ").lower()

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "add":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == "subtract":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == "divide":
    print(f"{num1} / {num2} = {divide(num1, num2)}") 

# Task 3: Ensure your code can handle division by zero and other potential errors.

operation = input("What operation would you like to perform? Add, subtract, multiply, or divide? ").lower()

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try: 
    num1 = int(num1)
except:
    num1 = float(num1)

try:
    num2 = int(num2)
except:
    num2 = float(num2)

if operation == "add":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif operation == "subtract":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif operation == "multiply":
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif operation == "divide":
    try:
        print(f"{num1} / {num2} = {divide(num1, num2)}") 
    except ZeroDivisionError:
        print("You can't divide by 0.")

# So if you divide by 0, there is error handling set up to prevent an error from showing in the console.