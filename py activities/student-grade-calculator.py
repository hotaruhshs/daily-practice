# student grade calculator
# average score of 3 scores and calculate the grade
# grade is A, B, C, D, F
# if the score is 90-100, the grade is A
# if the score is 80-89, the grade is B
# if the score is 70-79, the grade is C
# if the score is 60-69, the grade is D
# if the score is below 60, the grade is F

def calculate_grade(score):
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    else:
        return "F"

students_number = int(input("Enter the number of students: "))
for i in range(students_number):
    score1 = int(input(f"Enter the first score of student {i+1}: "))
    score2 = int(input(f"Enter the second score of student {i+1}: "))
    score3 = int(input(f"Enter the third score of student {i+1}: "))
    score = (score1 + score2 + score3) / 3
    print(f"The average score of student {i+1} is {score:.2f}")
    print(f"The grade of student {i+1} is {calculate_grade(score)}")

