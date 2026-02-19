# Create a program that calculates income tax based on the following slabs:
# • Up to ₹2,50,000 → No tax
# • ₹2,50,001 – ₹5,00,000 → 5%
# • ₹5,00,001 – ₹10,00,000 → 20%
# • Above ₹10,00,000 → 30%
# Additionally, if the person is a senior citizen (age ≥ 60), increase the exemption limit to ₹3,00,000.


age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
if age >= 60:
    ex_limit = 300000
else:    
    ex_limit = 250000

if income <= ex_limit:   
    tax = 0
elif income <= 500000:   
    tax = (income - ex_limit) * (5/100)
elif income <= 1000000:   
    tax = (income - 500000) * (20/100) + (500000 - ex_limit) * (5/100)
else:    
    tax = (income - 1000000) * (30/100) + (1000000 - 500000) * 0.20 + (500000 - ex_limit) * 0.05

print("Your income tax is: ₹", tax)