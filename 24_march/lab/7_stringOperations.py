names = ['anuj', 'rahul', 'sneha', 'kiran', 'amit']
s = pd.Series(names)

print(s.str.upper())

print(s[s.str.contains('a')])

s.replace('anuj', 'Anuj Kumar', inplace=True)
print(s)