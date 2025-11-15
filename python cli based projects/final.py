import random

print("""Welcome to the Number Guessing Game
I am thinking of a number between 1 and 100""")

print("""Please select the difficulty level:
1. Easy   (10 chances)
2. Medium (5 chances)
3. Hard   (3 chances)""")

def difficulty():
        choice = int(input("Enter your choice: "))
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter 1, 2 or 3")
            return difficulty()
        if choice == 1:
            print("Great! You have selected the easy difficulty level.")
            print("You have 10 attempts to guess the number")
            return 10
        elif choice == 2:
            print("Great! You have selected the medium difficulty level.")
            print("You have 5 attempts to guess the number")
            return 5
        elif choice == 3:
            print("Great! You have selected the hard difficulty level.")
            print("You have 3 attempts to guess the number")
            return 3
        else:
            print("Invalid choice")
            return difficulty()

def game():
    number = random.randint(1, 100)
    attempts = 0
    number_of_attempts = difficulty()
    return number, attempts, number_of_attempts

def play():
    number, attempts, number_of_attempts = game()
    print("Let's start the game!")
    while attempts < number_of_attempts:
        guess = int(input("Enter your guess: "))
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number between 1 and 100")
            continue
        if guess == number:
            print("Congratulations! You guessed the number correctly!")
            print(f"You guessed the number in {attempts} attempts.")
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
        
    print(f"You lost! The number was {number}.")
    try_again()

def try_again():
    while True:
        print("Thank you for playing. Do you want to play again? (y/n)")
        choice = input("Enter your choice: ")
        if choice == "y":
            play()
        elif choice == "n":
            print("Thank you for playing")
            break
        else:
            print("Invalid choice")
            try_again()

play()