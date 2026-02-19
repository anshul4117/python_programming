# 10.Write a program to calculate the average of three numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if(num1 < 0 or num2 < 0 or num3 < 0):
    print("Please enter positive Number .")
else:    
    average = (num1 + num2 + num3) / 3
    print("The average of", num1, ",", num2, "and", num3, "is : ", average)