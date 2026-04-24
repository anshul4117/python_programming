# 4. Salary Increment System
# An employee’s increment depends on:
# • Performance rating (1–5)
# • Years of experience
# • Attendance percentage
# Design logic to calculate increment percentage based on these factors.
# Input employee details

performance_rating = int(input("Enter performance rating (1-5): "))
years_experience = int(input("Enter years of experience: "))
attendance_percentage = float(input("Enter attendance percentage (0-100): "))
current_salary = float(input("Enter current salary: "))

increment_percentage = 0

if performance_rating == 5:
    increment_percentage = increment_percentage + 15
else:
    if performance_rating == 4:
        increment_percentage = increment_percentage + 10
    else:
        if performance_rating == 3:
            increment_percentage = increment_percentage + 5
        else:
            increment_percentage = increment_percentage + 0


if years_experience >= 10:
    increment_percentage = increment_percentage + 8
else:
    if years_experience >= 5:
        increment_percentage = increment_percentage + 5
    else:
        if years_experience >= 2:
            increment_percentage = increment_percentage + 2
        else:
            increment_percentage = increment_percentage + 0


if attendance_percentage >= 95:
    increment_percentage = increment_percentage + 5
else:
    if attendance_percentage >= 85:
        increment_percentage = increment_percentage + 3
    else:
        if attendance_percentage >= 75:
            increment_percentage = increment_percentage + 1
        else:
            increment_percentage = increment_percentage + 0



increment_amount = (current_salary * increment_percentage) / 100
new_salary = current_salary + increment_amount

print("Performance Rating:", performance_rating)
print("Years of Experience:", years_experience)
print("Attendance Percentage:", attendance_percentage)
print("Total Increment Percentage:", increment_percentage)
print("Current Salary:", current_salary)
print("Increment Amount:", increment_amount)
print("New Salary:", new_salary)

# output
# Enter performance rating (1-5): 4
# Enter years of experience: 6
# Enter attendance percentage (0-100): 90
# Enter current salary: 50000
# Performance Rating: 4
# Years of Experience: 6
# Attendance Percentage: 90.0
# Total Increment Percentage: 18
# Current Salary: 50000.0
# Increment Amount: 9000.0
# New Salary: 59000.0   
