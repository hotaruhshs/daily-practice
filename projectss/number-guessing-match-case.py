#number guessing using MATCH-CASE (09-01-2025)
import random

name = input("Enter your name: ")
number = random.randint(1, 20) 
attempts = 0

while True:
    guess = int(input(f"{name}, Guess the number between 1 and 20: "))
    
    match guess:
        case guess if guess == number:
            print(f"{name}, You guessed the number correctly in {attempts} attempts")
            attempts += 1
            break
        case guess if guess < number:
            print(f"{name}, You guessed the number too low")
            attempts += 1
        case guess if guess > number:
            print(f"{name}, You guessed the number too high")
            attempts += 1
        case _:
            print(f"{name}, You guessed the number incorrectly")
            attempts += 1
