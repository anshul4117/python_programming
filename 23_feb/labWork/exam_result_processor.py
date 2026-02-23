score_input = input("Enter student scores separated by space: ")

values = score_input.split()
scores = []

# Convert to integers
for v in values:
    scores.append(int(v))

# Remove lowest score (first time)
lowest_index = 0
for i in range(len(scores)):
    if scores[i] < scores[lowest_index]:
        lowest_index = i

scores.pop(lowest_index)

# Remove lowest score (second time)
lowest_index = 0
for i in range(len(scores)):
    if scores[i] < scores[lowest_index]:
        lowest_index = i

scores.pop(lowest_index)

# Add grace marks
for i in range(len(scores)):
    if scores[i] >= 30 and scores[i] <= 35:
        scores[i] = scores[i] + 5

# Count passed students
passed = 0
for i in range(len(scores)):
    if scores[i] >= 40:
        passed = passed + 1

print("Passed Students:", passed)