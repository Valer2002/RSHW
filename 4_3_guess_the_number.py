import random

target_number = random.randint(1, 100)
print("The computer picked a number between 1 and 100. Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < target_number:
        print("The target number is HIGHER.")
    elif guess > target_number:
        print("The target number is LOWER.")
    else:
        print("Congratulations! You guessed the number.")
        break
