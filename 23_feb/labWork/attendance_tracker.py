attendance_input = input("Enter attendance (1=Present, 0=Absent): ")

attendance = []
for value in attendance_input.split():
    attendance.append(int(value))
    
percentage = (sum(attendance) / len(attendance)) * 100
print("Attendance Percentage:", percentage)

if percentage < 75:
    print("Warning: Below 75% attendance")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance:", attendance)