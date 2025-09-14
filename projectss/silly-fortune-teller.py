import random

# def fortune_teller():
#     characters = ["a ninja cat", "a space pirate", "a llama", "a wizard", "a robot duck"]
#     places = ["the moon", "your fridge", "a volcano", "the desert", "a haunted library"]
#     actions = ["dance forever", "eat spaghetti", "sing badly", "rule the squirrels", "fight boredom"]

#     print(f"{name}, in the future you will meet {random.choice(characters)} on {random.choice(places)} and together you will {random.choice(actions)}")

# print("Welcome to the Silly Fortune Teller")
# name = input("Enter your name: ")

# choices = input(f"Hello {name}, do you want to know your fortune? (y/n) ").lower()
# if choices == "y":
#     fortune_teller()
# else:
#     print("Thank you for playing")

def character():
    characters = ["a ninja cat", "a space pirate", "a llama", "a wizard", "a robot duck"]
    return random.choice(characters)

def places():
    places = ["the moon", "your fridge", "a volcano", "the desert", "a haunted library"]
    return random.choice(places)

def actions():
    actions = ["dance forever", "eat spaghetti", "sing badly", "rule the squirrels", "fight boredom"]
    return random.choice(actions)

def fortune_teller():
    print(f"{name}, in the future you will meet {character()} on {places()} and together you will {actions()}")

print("Welcome to the Silly Fortune Teller")
name = input("Enter your name: ")

while True:
    choices = input(f"Hello {name}, do you want to know your fortune? (y/n) ").lower()
    if choices == "y":
        fortune_teller()
    elif choices == "n":
        print("Thank you for playing")
        break
    else:
        print("Invalid choice")
        continue