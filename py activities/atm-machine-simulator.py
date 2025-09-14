
# wassup
# atm machine simulator

def atm_machine():
    balance = 0
    print("Welcome to the Bank")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(f"Your balance is {balance}")
        elif choice == 2:
            amount = int(input("Enter the amount to deposit: "))
            balance += amount
            print(f"Your new balance is {balance}")
        elif choice == 3:
            amount = int(input("Enter the amount to withdraw: "))
            if balance < amount:
                print("You don't have enough balance")
                continue
            elif amount % 100 != 0:
                print("The amount must be a multiple of 100")
                continue
            else:
                balance -= amount
            print(f"Your new balance is {balance}")
        elif choice == 4:
            print("Thank you for using the Bank")
            break
        else:
            print("Invalid choice")

atm_machine()
