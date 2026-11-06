a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

print(f"Sum (a + b) = {a + b}")
print(f"Difference (a - b) = {a - b}")
print(f"Product (a * b) = {a * b}")

if b != 0:
    print(f"Quotient (a / b) = {a / b}")
else:
    print("Error: Division by zero is not allowed.")
