# Q13: Filter dictionary to keep only entries where value is above a threshold
# Input: {"math": 85, "science": 40, "english": 72, "hindi": 35, "history": 90}
# Threshold: 50
# Output: {"math": 85, "english": 72, "history": 90}

marks = {"math": 85, "science": 40, "english": 72, "hindi": 35, "history": 90}
threshold = 50

passed = {}
for subject, score in marks.items():
    if score >= threshold:
        passed[subject] = score

print("All Marks:", marks)
print("Threshold:", threshold)
print("Passed Subjects:", passed)

# Output:
# All Marks: {'math': 85, 'science': 40, 'english': 72, 'hindi': 35, 'history': 90}
# Threshold: 50
# Passed Subjects: {'math': 85, 'english': 72, 'history': 90}
