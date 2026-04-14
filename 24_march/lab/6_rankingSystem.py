scores = [88, 92, 79, 93, 85]
players = ['P1','P2','P3','P4','P5']

s = pd.Series(scores, index=players)

ranks = s.rank(ascending=False)
print(ranks)

print(s.sort_values(ascending=False).head(3))

print(s.idxmin(), s.min())