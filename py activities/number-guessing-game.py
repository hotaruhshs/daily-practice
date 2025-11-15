import random

number = random.randint(1, 50)
attempts = 0
number_of_attempts = 5

while True:
    guess = int(input("Guess the number (1-50): "))
    if guess == number:
        print(f"Correct! You guessed the number in {attempts} attempts!")
        break
    elif guess < number:
        print("Too low!")
        attempts += 1
        print(f"You have {number_of_attempts - attempts} attempts left!")
        if attempts >= number_of_attempts:
            print(f"You lost! The number was {number}.")
            break
    else:
        print("Too high!")
        attempts += 1
        print(f"You have {number_of_attempts - attempts} attempts left!")
        if attempts >= number_of_attempts:
            print(f"You lost! The number was {number}.")
            break

