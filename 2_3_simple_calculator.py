num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    result = num1 + num2
    print(f"Result: {result}")
elif op == '-':
    result = num1 - num2
    print(f"Result: {result}")
elif op == '*':
    result = num1 * num2
    print(f"Result: {result}")
elif op == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Error: Division by zero.")
else:
    print("Unknown operator.")
