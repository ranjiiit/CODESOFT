# Task 1. is :- Simple Calculator

print("Simple Calculator")
print("-----------------")

#  we will taking  Input of  two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# ask to user for  operation
op = input("Enter operation (+, -, *, /): ")

# from here calculation start Performing.
if op == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif op == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif op == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operation choice!")
