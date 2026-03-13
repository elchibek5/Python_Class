# 1. Calculator for Area and Perimeter
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating the area and perimeter
area = length * width
perimeter = 2 * (length + width)

print(f"The area of the rectangle is {area} and the perimeter is {perimeter}.")


# 2. Interest Calculator
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time in years: "))

# Calculate interest
simple_interest = (principal * rate * time) / 100

# Calculate total amount
total_amount = principal + simple_interest

print(
    f"The simple interest is {simple_interest} and the total amount after {time} years will be {total_amount}."
)
