# Simple Bill Calculator

# Write a Python program that asks the user for:

# Product name
# Product price
# Quantity

# Then calculate and display the total bill.

# Example
# Enter product name: Pen
# Enter price: 20
# Enter quantity: 5

# Product: Pen
# Price: ₹20
# Quantity: 5
# Total: ₹100

product = input("Enter the name of the product: ")
price = float(input("Enter the price of the product: "))
quantity = float(input("Enter the quantity of the product: "))

print(f'''
Bill:-
Product name: {product}
Price: {price}
Quantity: {quantity}
Total Amount: {price * quantity}
----END----
''')