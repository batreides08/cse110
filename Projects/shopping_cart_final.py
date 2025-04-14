"""
Author: Bryan Quiros
Purpose: To provide a full shopping cart item list with the final price

"""
# Shopping Cart - FINAL VERSION

cart_items = []
cart_prices = []

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
        price = input(f"What is the price of '{item}'? ")
        try:
            price = float(price)
            cart_items.append(item)
            cart_prices.append(price)
            print(f"'{item}' has been added to the cart.")
        except ValueError:
            print("Invalid price. Item not added.")
    
    elif choice == "2":
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")

    elif choice == "3":
        print("\nThe contents of the shopping cart are:")
        for i in range(len(cart_items)):
            print(f"{i + 1}. {cart_items[i]} - ${cart_prices[i]:.2f}")
        index = input("Which item would you like to remove? ")
        if index.isdigit():
            index = int(index) - 1  # convert to 0-based index
            if 0 <= index < len(cart_items):
                removed_item = cart_items.pop(index)
                cart_prices.pop(index)
                print(f"{removed_item} removed.")
            else:
                print("Sorry, that is not a valid item number.")
        else:
            print("Invalid input. Please enter a number.")
    
    elif choice == "4":
        total = sum(cart_prices)
        print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")

    elif choice == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid choice. Please try again.")