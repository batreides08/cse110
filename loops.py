payment = float(input("What is the payment amount? "))

while payment < 0:
    print("Sorry the payment can't be negative.")

    payment = float(input("What is the payment amount? "))

print(f"The amount is ${payment:.2f}")