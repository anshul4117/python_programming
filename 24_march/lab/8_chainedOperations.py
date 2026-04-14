data = [5, None, 15, 25, None, 35, 45]
s = pd.Series(data)

result = (
    s.fillna(s.median())   # fill median
     .loc[lambda x: x > 20] # filter > 20
     .sort_values(ascending=False) # sort desc
     .reset_index(drop=True) # reset index
)

print(result)