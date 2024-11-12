print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" 1. Espresso")
print(" 2. Americano")
print(" 3. Latte")
print(" 4. Cappuccino")
print(" 5. Macchiato")
print(" 6. Mocha")
print(" 7. Flat White")
print("----------------------------")

# Coffee menu with prices
coffee_menu = {
    "1": ("Espresso", 2.50),
    "2": ("Americano", 3.00),
    "3": ("Latte", 2.50),
    "4": ("Cappuccino", 3.50),
    "5": ("Macchiato", 3.00),
    "6": ("Mocha", 3.50),
    "7": ("Flat White", 3.00)
}

# Valid size options
size_options = {"M": 0, "L": 1.00, "XL": 1.50}

# Get the number of cups
total_cost = 0
num_cups = input("How many cups of coffee would you like? ")
while not num_cups.isdigit() or int(num_cups) <= 0:
    print("Please enter a valid number of cups.")
    num_cups = input("How many cups of coffee would you like? ")
num_cups = int(num_cups)

# Loop through each cup of coffee order
for i in range(num_cups):
    print(f"\nOrder for cup #{i + 1}:")
    
    # Get coffee choice with validation
    coffee_choice = input("Please enter the number of the coffee you would like: ")
    while coffee_choice not in coffee_menu:
        print("Invalid choice. Please select a number between 1 and 7.")
        coffee_choice = input("Please enter the number of the coffee you would like: ")
    
    # Retrieve coffee name and price
    coffee_name, coffee_price = coffee_menu[coffee_choice]
    cup_cost = coffee_price

    # Get cup size with validation
    size = input("What size would you like? (M / L / XL) ").upper()
    while size not in size_options:
        print("Invalid size. Please enter M for Medium, L for Large, or XL for Extra Large.")
        size = input("What size would you like? (M / L / XL) ").upper()
    
    # Add extra cost based on size
    cup_cost += size_options[size]

    # Get eat-in or takeaway preference with validation
    takeaway = input("Would you like to take away? (Yes / No) ").title()
    while takeaway not in ["Yes", "No"]:
        print("Invalid option. Please enter Yes or No.")
        takeaway = input("Would you like to take away? (Yes / No) ").title()

    # Display individual order summary and add to total
    print(f"Order Summary for cup #{i + 1}: {size} {coffee_name} - {'Take Away' if takeaway == 'Yes' else 'Eat In'}")
    print(f"Cost for this cup: £{cup_cost:.2f}")
    total_cost += cup_cost

# Display final total
print("\n----------------------------")
print(f"Total Cost for {num_cups} cup(s): £{total_cost:.2f}")
