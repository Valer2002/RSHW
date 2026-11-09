import random

secret = random.randint(1, 100)

print("Ես ընտրել եմ թիվ 1-ից 100։ Փորձիր գուշակել։")

while True:
    guess = int(input("Մուտքագրիր քո տարբերակը։ "))

    if guess > secret:
        print("Քո թիվը մեծ է պահված թվից։")
    elif guess < secret:
        print("Քո թիվը փոքր է պահված թվից։")
    else:
        print("Ճիշտ է։ Դու գուշակեցիր։")
        break
