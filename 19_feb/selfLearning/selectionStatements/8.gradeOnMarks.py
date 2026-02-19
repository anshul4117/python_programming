# 8.Write a program to calculate grade based on marks:
#     ⏺ 90+ → A
#     ⏺ 75–89 → B
#     ⏺ 50–74 → C
#     ⏺ Below 50 → Fail

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")   
elif marks >= 50:
    print("Grade: C")
else:    
    print("Grade: Fail")