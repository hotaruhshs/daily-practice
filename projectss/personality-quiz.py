#personality quiz (09-01-2025)

name = input("Enter your name: ")
points = 0

print(f"Hello {name}, Welcome to the personality quiz!")
print("\n")
q1 = input("What is your favorite color? A. Blue, B. Red, C. Green, D. Yellow: ")
if q1 == "blue":
    points += 1 #adds 1 to the points 
    # += is an augmented assignment operator, it means points = points + 1
elif q1 == "red":
    points += 2 #adds 2 to the points #points = points + 2
elif q1 == "green":
    points += 3 #adds 3 to the points #points = points + 3
elif q1 == "yellow":
    points += 4 #adds 4 to the points #points = points + 4
else:
    print("Invalid answer")

q2 = input("What is your favorite food? A. Pizza, B. Burger, C. Salad, D. Pasta: ")
if q2 == "pizza":
    points += 1 
elif q2 == "burger":
    points += 2 
elif q2 == "salad":
    points += 3 
elif q2 == "pasta":
    points += 4 
else:
    print("Invalid answer")

q3 = input("What is your favorite animal? A. Dog, B. Cat, C. Bird, D. Fish: ")
if q3 == "dog":
    points += 1 
elif q3 == "cat":
    points += 2 
elif q3 == "bird":
    points += 3 
elif q3 == "fish":
    points += 4 
else:
    print("Invalid answer")

q4 = input("What is your favorite hobby? A. Reading, B. Writing, C. Painting, D. Music: ")
if q4 == "reading":
    points += 1 
elif q4 == "writing":
    points += 2 
elif q4 == "painting":
    points += 3 
elif q4 == "music":
    points += 4 
else:
    print("Invalid answer")

if points >= 10:
    print(f"{name}, You are a nerd")
elif points >= 20:
    print(f"{name}, You are a cool person")
elif points >= 30:
    print(f"{name}, You are a funny person")
else:
    print(f"{name}, You are a boring person")