# 3. E-commerce Discount Engine
# An online shopping platform gives discounts based on:
# • Cart value
# • Customer membership (Silver/Gold/Platinum)
# • Festival season
# Apply the highest eligible discount and print the final payable amount without using the functions and simple way.

cart_value = float(input("Enter the cart value: "))
membership = input("Enter your membership type (Silver/Gold/Platinum): ")
festival = input("Is it a festival season? (yes/no): ")

discount_percentage = 0

if membership.lower() == "silver":
    discount_percentage = 0.05
elif membership.lower() == "gold":
    discount_percentage = 0.10
elif membership.lower() == "platinum":
    discount_percentage = 0.15

if festival.lower() == "yes" and 0.10 > discount_percentage:
    discount_percentage = 0.10

discount = discount_percentage * cart_value
final_amount = cart_value - discount

print("Your final payable amount is: ₹", final_amount)