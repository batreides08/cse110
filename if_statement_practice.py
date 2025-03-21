# Ask the user for two integers
first = int(input("What is the first number? "))
second = int(input("What is the second number? "))

# Check if the first number is greater than the second
if first > second:
    print("The first number is greater")
else:
    print("The first number is not greater")

# Check if the two numbers are equal
if first == second:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

# Check if the second number is greater than the first
if second > first:
    print("The second number is greater")
else:
    print("The second number is not greater")

print()

# Ask the user for their favorite animal
animal = input("What is your favorite animal? ")

if animal.lower() == "dog":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")