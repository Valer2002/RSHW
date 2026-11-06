def is_even(number):
    return number % 2 == 0

num = int(input("Enter an integer: "))

if is_even(num):
    print(f"{num} is Even (True)")
else:
    print(f"{num} is Odd (False)")
