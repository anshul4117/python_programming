# 10.Write a program to check whether a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if(age <=0):
    print("Invalid age")
else:
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")