
#ASK USER
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))


subtotal = (child_price * children) + (adult_price * adults)
print(f"Subtotal ${subtotal}")
