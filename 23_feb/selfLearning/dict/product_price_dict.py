products = {}

n = int(input("How many products? "))

for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    products[name] = price

print("Product List:", products)