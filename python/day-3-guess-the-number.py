import random

random_num = random.randint(1, 10)
guess = int(input("Guess the number (1-10): "))

while True:
    if random_num == guess:
     print("You guess it!")
     break
    elif random_num < guess:
     print("Too high!")
     guess = int(input("Guess the number (1-10): "))
    else:
     print("Too low!")
     guess = int(input("Guess the number (1-10): "))
