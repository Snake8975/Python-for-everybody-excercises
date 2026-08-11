# Retrieving user inputs, hours and rate, for calculating pay, fixed with overtime pay if applicable.
varGrade = float(input("Enter grade: ")) # Retrieve grade from user

if varGrade < 0 or varGrade > 1:
    print("Invalid grade entered. Enter a number between 0 and 1.")
elif varGrade >= 0.9:
    print("A")
elif varGrade >= 0.8:
    print("B")
elif varGrade >= 0.7:
    print("C")
elif varGrade >= 0.6:
    print("D")
else:
    print("F")                 
