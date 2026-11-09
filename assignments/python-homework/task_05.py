a = float(input("Մուտքագրիր առաջին թիվը։ "))
b = float(input("Մուտքագրիր երկրորդ թիվը։ "))
action = input("Մուտքագրիր գործողությունը՝ +, -, *, /։ ")

if action == "+":
    print("Արդյունքը՝", a + b)
elif action == "-":
    print("Արդյունքը՝", a - b)
elif action == "*":
    print("Արդյունքը՝", a * b)
elif action == "/":
    if b != 0:
        print("Արդյունքը՝", a / b)
    else:
        print("Զրոյի բաժանել հնարավոր չէ։")
else:
    print("Սխալ գործողություն։")
