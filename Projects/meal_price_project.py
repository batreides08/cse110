#ASK USER
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

#SUBTOTAL
subtotal = (child_price * children) + (adult_price * adults)
print(f"Subtotal ${subtotal:.2f}")

#TAXES
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (tax_rate / 100) * subtotal
total = subtotal + sales_tax
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")

#CHANGE
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")