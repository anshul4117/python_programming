salary = [25000, 32000, 28000, 40000, 50000]
emp = ['A', 'B', 'C', 'D', 'E']

s = pd.Series(salary, index=emp)

s[s < 30000] = s[s < 30000] * 1.10

s[s > 45000] = s[s > 45000] * 0.95

print(s.sum())
print(s)