salaries = list(map(int, input("Enter salaries: ").split()))

valid_salaries = []
for s in salaries:
    if s >= 10000:   # minimum wage
        if s > 50000:
            s = s + (0.05 * s)
        valid_salaries.append(s)

valid_salaries.sort(reverse=True)

print("Top 3 Salaries:", valid_salaries[:3])