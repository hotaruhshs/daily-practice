import random

print("""Welcome to the Number Guessing Game
I am thinking of a number between 1 and 100""")

print("""Please select the difficulty level:
1. Easy   (10 chances)
2. Medium (5 chances)
3. Hard   (3 chances)

Type 'exit' to quit the game""")

easy = 10
medium = 5
hard = 3
number = random.randint(1, 100)
attempts = 0
number_of_attempts = 0

def difficulty_level():
        difficulty = int(input("Enter your choice: "))
        if difficulty == 1:
            print("Great! You have selected the easy difficulty level.")
            print(f"You have {easy} attempts to guess the number")
            number_of_attempts = easy
        elif difficulty == 2:
            print("Great! You have selected the medium difficulty level.")
            print(f"You have {medium} attempts to guess the number")
            number_of_attempts = medium
        elif difficulty == 3:
            print("Great! You have selected the hard difficulty level.")
            print(f"You have {hard} attempts to guess the number")
            number_of_attempts = hard
        elif difficulty == "exit":
            print("Thank you for playing")
            exit()
            return
        else:
            print("Invalid choice")
            difficulty_level()

def game():
    print("Let's start the game!")

    while attempts < number_of_attempts:
        guess = int(input("Enter your guess: "))
        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            print(f"You guessed the number in {attempts} attempts")
            break
        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}")
            attempts += 1
        elif guess > number:
            print(f"Incorrect! The number is less than {guess}")
            attempts += 1
        else:
            print("Invalid guess")
            continue
    print(f"You lost! The number was {number}")

def exit():
    print("Thank you for playing")
    exit()

difficulty_level()
game()
