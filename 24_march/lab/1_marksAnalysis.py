import pandas as pd

marks = [45, 67, 89, 34, 90, 55, 72]
subjects = ['Math', 'Physics', 'Chemistry', 'English', 'CS', 'Biology', 'History']

s = pd.Series(marks, index=subjects)

print(s[s > 70])

s_updated = s.copy()
s_updated[s_updated < 40] = "Fail"
print(s_updated)

avg = s.mean()
count = (s > avg).sum()
print(count)