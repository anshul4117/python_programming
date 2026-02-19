# 8.Write a program to calculate simple interest.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))
if(principal <= 0.0 or rate <= 0.0 or time <= 0.0):
    print("Principal, rate and time should be greater then 0.0")
else:
    simple_interest = (principal * rate * time) / 100
    print("The simple interest is:", simple_interest)
