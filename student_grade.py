# Student Grade Management System
# Student: Ephrata Elias
# Student ID: Bits/UGR/0192/24
# Programming Language: Python
# Development Environment: Visual Studio Code


# Function to validate student marks
def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Invalid mark! Enter a number between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# Validate student name
while True:
    student_name = input("Enter student name: ").strip()

    if student_name:
        break
    else:
        print("Student name cannot be empty.")


# Get student marks
math = get_valid_mark("Mathematics")
english = get_valid_mark("English")
physics = get_valid_mark("Physics")


# Calculate average
average = (math + english + physics) / 3


# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"


# Display results
print("\n--- Student Results ---")
print("Student Name:", student_name)
print("Mathematics:", math)
print("English:", english)
print("Physics:", physics)
print("Average Mark:", round(average, 2))
print("Letter Grade:", grade)