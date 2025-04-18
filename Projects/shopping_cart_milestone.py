# Shopping Cart Milestone

cart_items = []

print("Welcome to the Shopping Cart Program!")

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item") 
    print("4. Compute total")  
    print("5. Quit")

    choice = input("Please enter an action: ")

    if choice == "1":
        item = input("What item would you like to add? ")
        cart_items.append(item)
        print(f"'{item}' has been added to the cart.")
    elif choice == "2":
        print("\nThe contents of the shopping cart are:")
        for item in cart_items:
            print(item)
    elif choice == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")
