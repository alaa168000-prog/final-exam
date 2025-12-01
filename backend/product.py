products = [
    {"name": "Arabic Coffee", "price": 10.0},
    {"name": "Black Coffee", "price": 8.0},
    {"name": "Turkish Coffee", "price": 15.0},
    {"name": "Cappuccino", "price": 18.0},
    {"name": "Latte", "price": 20.0}
]

print("Product List:")
for i, product in enumerate(products, start=1):
    print(str(i) + ". " + product["name"] + " - Price: " + str(product["price"]) + " SAR")

choice_input = input("Enter the number of the product you want to check the price for: ")

if choice_input.isdigit():
    choice = int(choice_input)
    if 1 <= choice <= len(products):
        selected_product = products[choice - 1]
        price = selected_product["price"]
        tax = price * 0.15
        total_price = price + tax

        print("\nProduct: " + selected_product["name"])
        print("Price before tax: " + str(price) + " SAR")
        print("Tax (15%): " + str(round(tax, 2)) + " SAR")
        print("Total price including tax: " + str(round(total_price, 2)) + " SAR")
    else:
        print("The number you entered is invalid. Please enter a number from 1 to 5.")
else:
    print("Invalid input. Please enter a valid number.")
