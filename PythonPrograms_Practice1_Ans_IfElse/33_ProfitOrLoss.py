# Program to calculate profit or loss

# Input cost price and selling price
cost_price = float(input("Enter the cost price: "))
selling_price = float(input("Enter the selling price: "))

# Calculate and display profit or loss
if selling_price > cost_price:
    print(f"Profit: {selling_price - cost_price}")
elif selling_price < cost_price:
    print(f"Loss: {cost_price - selling_price}")
else:
    print("No profit, no loss.")
