name = "John"
age = 20
if name == "John" and age == 21:
    print("You are John and you are 20 years old")
else:
    print("You are not John or you are not 20 years old")

if name == "John" or name == "Jane":
    print("You are John or Jane")
else:
    print("You are not John or Jane")

if name in ["John", "Jane"]:
    print("You are John or Jane")
else:
    print("You are not John or Jane")

# range(start, stop, increment)
for x in range(3, 8, 2):
    print(x)

for x in range (10):
    if x % 2 == 0:
        continue
    print(x)

