def myFunction(name, age):
    print("Hello", name, "you are", age, "years old")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
myFunction(name, age)

def myFunction(name, age):
    return f"Hello {name}, you are {age} years old"

name = input("Enter your name: ")
age = int(input("Enter your age: "))

greeting = myFunction(name, age)  # save what the function returned
print(greeting)                   # we decide *when* to print it