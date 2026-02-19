# 2.Write a program to subtract two numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if(num1 < 0 or num2 < 0):
    print("Please enter positive numbers only.")
else:
    result = num1 - num2
    print("The difference of num1 and num2 is: ", result)