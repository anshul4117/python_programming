
students = [
    ("Alice", 85), 
    ("Bob", 92), 
    ("Charlie", 78), 
    ("David", 88)
    ]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Original list:", students)
print("Sorted by marks:", sorted_students)