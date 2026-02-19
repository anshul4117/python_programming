# 4.Write a program to find the largest of two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if(num1 < 0 or num2 < 0):
    print("Negative numbers are not allowed.")
else:
    if num1 > num2:
        print(num1, "is the largest number.")
    elif num2 > num1:
        print(num2, "is the largest number.")
    else:    
        print("Both numbers are equal.")       
