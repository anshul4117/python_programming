marks = list(map(int, input("Enter student marks separated by space: ").split()))

# Remove invalid marks
valid_marks = []
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)

if len(valid_marks) == 0:
    print("No valid marks entered.")
else:
    avg = sum(valid_marks) / len(valid_marks)
    topper = max(valid_marks)

    print("Average:", avg)
    print("Topper Marks:", topper)

    if avg >= 90:
        print("Grade: A")
    elif avg >= 75:
        print("Grade: B")
    elif avg >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")