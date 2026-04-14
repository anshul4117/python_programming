marks = [95, 82, 67, 58, 73, 49, 88]
students = ['S1','S2','S3','S4','S5','S6','S7']

s = pd.Series(marks, index=students)

def grade(m):
    if m >= 90:
        return 'A'
    elif m >= 75:
        return 'B'
    elif m >= 60:
        return 'C'
    else:
        return 'D'

grades = s.apply(grade)

print(grades)

print(grades.value_counts())