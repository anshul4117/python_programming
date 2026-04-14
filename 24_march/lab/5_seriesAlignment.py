s1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
s2 = pd.Series([5, 15, 25], index=['B', 'C', 'D'])

result = s1 + s2
print(result)

result_fixed = s1.add(s2, fill_value=0)
print(result_fixed)