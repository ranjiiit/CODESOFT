print("Simple Calculator")
print("-----------------")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


op = input("Enter operation (+, -, *, /): ")

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

