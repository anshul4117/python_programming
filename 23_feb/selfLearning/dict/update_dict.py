student = {}
name = input("Enter name: ")
marks = int(input("Enter marks: "))

student["name"] = name
student["marks"] = marks

student.update({"grade": "A"})   # using update()

print("Dictionary:", student)