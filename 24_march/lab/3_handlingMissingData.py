data = [10, None, 30, None, 50, 60, None]
s = pd.Series(data)

print(s.isnull().sum())

s_filled = s.fillna(s.mean())

print(s_filled.isnull().sum())

s_clean = s_filled.dropna()
print(s_clean)