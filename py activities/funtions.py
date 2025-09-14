def myFunction():
    print("Hello from my function.")

def myFunction_with_Arguments(username, greeting):
    print("Hello, %s, From my function!, I wish you %s" % (username, greeting))

def add(a, b):
    return a + b

myFunction()

myFunction_with_Arguments("John", "a great year!")
myFunction_with_Arguments("Hi", "a great year!")

x = add(5, 3)
print(x)