num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    print(num1, "+", num2, "=", num1 + num2)

if operation == "-":
    print(num1, "-", num2, "=", num1 - num2)

if operation == "*":
    print(num1, "*", num2, "=", num1 * num2)

if operation == "/":
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
