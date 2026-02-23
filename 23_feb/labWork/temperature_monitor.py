temps = list(map(int, input("Enter temperatures: ").split()))

hottest = temps[0]
coldest = temps[0]

for t in temps:
    if t > hottest:
        hottest = t
    if t < coldest:
        coldest = t

extreme_days = 0

# Replace above 45 and count extreme days
for i in range(len(temps)):
    if temps[i] > 40:
        extreme_days = extreme_days + 1

    if temps[i] > 45:
        temps[i] = "Heat Alert"

print("Hottest Day:", hottest)
print("Coldest Day:", coldest)
print("Extreme Days:", extreme_days)
print("Updated List:", temps)