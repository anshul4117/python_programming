prices = list(map(float, input("Enter product prices: ").split()))

prices = list(set(prices))   # remove duplicates
total = sum(prices)

if total > 5000:
    total = total - (0.10 * total)

gst = 0.18 * total
final_amount = total + gst

print("Final Payable Amount:", final_amount)