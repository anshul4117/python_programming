# 1. Electricity Bill Calculator
# Calculate the electricity bill based on units consumed:
# • 0–100 → ₹5/unit
# • 101–300 → ₹7/unit
# • Above 300 → ₹10/unit
# If the user is a senior citizen, apply 10% discount.

units = float(input("Enter units consumed: "))
is_senior = input("Are you a senior citizen? (yes/no): ").lower()

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

if is_senior == "yes":
    bill = bill * 0.9

print(f"Total Bill: ₹ ", bill)

# output
# Enter units consumed: 350
# Are you a senior citizen? (yes/no): yes
# Total Bill: ₹  3150.0