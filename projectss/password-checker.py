def password_checker():
    password = input("Enter your password: ")

    while True:
        if len(password) < 8:
            print("Password must be at least 8 characters long")
            password_checker()
        elif not any(password.isupper()for char in password ):
            print("Password must contain at least one uppercase letter")

        elif not any(password.islower()for char in password):
            print("Password must contain at least one lowercase letter")
            
        elif not any(password.isdigit()for char in password):
            print("Password must contain at least one number")
            
        else:
            print("Password is valid")
            break
password_checker()