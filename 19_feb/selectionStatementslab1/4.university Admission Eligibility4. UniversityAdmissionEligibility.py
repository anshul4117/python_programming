# 4. University Admission Eligibility
# A student applies for admission. Eligibility rules:
# • Minimum 75% in 12th grade
# • Must have studied Mathematics
# • Entrance exam score ≥ 80
# If any condition fails, show the exact reason.


grade_12_percentage = float(input("Enter your 12th grade percentage: "))
studied_math = input("Did you study Mathematics? (yes/no): ").lower()
entrance_score = float(input("Enter your entrance exam score: "))

eligible = True

if grade_12_percentage < 75:
    print("• 12th grade percentage is below 75%")
    eligible = False

if studied_math != "yes":
    print("• Mathematics was not studied")
    eligible = False

if entrance_score < 80:
    print("• Entrance exam score is below 80")
    eligible = False

if eligible:
    print("Congratulations! You are eligible for admission.")
else:
    if grade_12_percentage < 75 or studied_math != "yes" or entrance_score < 80:
        print("You are not eligible. Reasons:")
