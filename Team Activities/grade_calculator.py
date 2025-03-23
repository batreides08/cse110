"""
Author: Bryan Quiros
Purpose: Calculate and display grades
"""


grade_percent = float(input("Please enter your grade percentage: "))

letter = ""

if grade_percent >= 90:
    letter = "A"
elif grade_percent >= 80:
    letter = "B"
elif grade_percent >= 70:
    letter = "C"
elif grade_percent >= 60:
    letter = "D"
else:
    letter = "F"

# Challenge 1
sign = ""

last_digit = grade_percent % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Challenge 2
if grade_percent >= 93:
    sign = ""

# Challenge 3
if letter == "F":
    sign = ""


print(f"Your grade is {letter}{sign}. ")

if grade_percent  >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Keep working hard! You can do better next time.")

