stock = list(map(int, input("Enter stock quantities: ").split()))

updated_stock = []

for s in stock:
    if s > 0:
        if s < 10:
            s += 50
        updated_stock.append(s)

print("Total Inventory:", sum(updated_stock))