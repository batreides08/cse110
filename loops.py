payment = float(input("What is the payment amount? "))

while payment < 0:
    print("Sorry the payment can't be negative.")

    payment = float(input("What is the payment amount? "))

    print("...")
    print("...")
    print("...")
    print("...")

    #jump back to line 3

print(f"The amount is ${payment:.2f}")