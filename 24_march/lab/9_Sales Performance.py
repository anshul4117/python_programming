sales = [200, 450, 300, 150, 500, 700, 100]
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

s = pd.Series(sales, index=days)

print("Best:", s.idxmax(), s.max())
print("Worst:", s.idxmin(), s.min())

print("Total:", s.sum())
print("Average:", s.mean())

bonus = s.copy()
bonus[bonus > 400] = bonus[bonus > 400] * 1.20
print(bonus)

print(s.sort_values(ascending=False))