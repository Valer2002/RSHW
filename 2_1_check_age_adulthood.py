age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
elif age >= 0:
    print("You are a minor.")
else:
    print("Invalid input: Age cannot be negative.")
