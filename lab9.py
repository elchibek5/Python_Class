# Task 1
shopping_prices = {
    "Apple": 3.08,
    "Mango": 2.79,
    "Meat": 6.89,
    "Juice": 5.34,
    "Chips": 3.76,
    "Soda": 2.09
}

total_shopping_cost = sum(shopping_prices.values())

print(f"Task 1 - Total Shopping Cost: ${total_shopping_cost:.2f}")
print("-" * 30)

# Task 2
stationary_items = {
    "Pen": 1.25,
    "Notebook": 2.60,
    "Folder": 1.99,
    "Pencil": 0.89,
    "Eraser": 0.50,
    "Marker": 2.20
}

purchase_quantities = {
    "Pen": 2,
    "Notebook": 1,
    "Pencil": 3,
    "Marker": 1
}

total_bill = 0
for item, quantity in purchase_quantities.items():
    total_bill += stationary_items[item] * quantity

print("Task 2 - Student Stationary Bill")
for item, qty in purchase_quantities.items():
    subtotal = stationary_items[item] * qty
    print(f"{item}: {qty} @ ${stationary_items[item]} each = ${subtotal:.2f}")

print("-" * 30)
print(f"Total Bill: ${total_bill:.2f}")