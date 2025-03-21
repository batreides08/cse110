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

sign = ""

if letter != "F":  # F+, and F-
    last_digit = int(grade_percent) % 10  # get the last digit

    if last_digit >= 7 and letter != "A": # ignore A- or A+
        sign = "+"
    elif last_digit < 3:
        sign = "-"


print(f"Your grade is {letter}{sign}. ")

if grade_percent  >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Keep working hard! You can do better next time.")

