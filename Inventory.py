# Manages products with prices and calculates total cost
# Create a dictionary of products and prices
products = {
    "Laptop": 80000,
    "Mouse": 1500,
    "Keyboard": 3000
}

# Print all products with prices
print("Product List:")
for product, price in products.items():
    print(product, ":", price)

# Add a new product
products["Headphones"] = 5000

# Update the price of one product
products["Mouse"] = 1800

# Print updated product list
print("\nUpdated Product List:")
for product, price in products.items():
    print(product, ":", price)

# Calculate total price
total_price = sum(products.values())
print("\nTotal Price of All Products:", total_price)