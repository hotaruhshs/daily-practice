def calculator():
    print ("CALCULATOR")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
    print ("5. Exit")

while True:
    calculator()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} + {num2} = {num1 + num2}")
        calculator()
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} - {num2} = {num1 - num2}")
        calculator()
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} * {num2} = {num1 * num2}")
        calculator()
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} / {num2} = {num1 / num2}")
        calculator()
    elif choice == 5:
        break
    else:
        print("Invalid choice")