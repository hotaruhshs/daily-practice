#conditionals (09-01-2025)
name = input("Enter your name: ")
grade = int(input("Enter your grade: "))

if grade >= 90:
    print(f"{name}, You are a genius") #f-string is used to format the string instead of using %s or %d
elif grade >= 80:
    print(f"{name}, You are a good student")
elif grade >= 70:
    print(f"{name}, You are a average student")
else:
    print(f"{name},  You are a bad student")