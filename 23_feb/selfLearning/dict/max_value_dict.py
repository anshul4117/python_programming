marks = {
    "Rahul": 85,
    "Anshul": 90,
    "Aman": 78
}

highest = 0
topper = ""

for name in marks:
    if marks[name] > highest:
        highest = marks[name]
        topper = name

print("Topper:", topper)
print("Marks:", highest)