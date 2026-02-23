transaction_input = input("Enter transactions separated by space: ")

transactions = []
values = transaction_input.split()

for v in values:
    transactions.append(int(v))

balance = 0
largest_withdrawal = 0
large_deposits = 0

for t in transactions:
    balance = balance + t

    if t < 0:
        if largest_withdrawal == 0 or t < largest_withdrawal:
            largest_withdrawal = t

    if t > 10000:
        large_deposits = large_deposits + 1

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", large_deposits)