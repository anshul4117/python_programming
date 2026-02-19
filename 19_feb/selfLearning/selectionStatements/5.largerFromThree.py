# 5.Write a program to find the largest of three numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if(num1 < 0 or num2 < 0 or num3 < 0):
    print("Negative numbers are not allowed.")
else:
    if num1 > num2 and num1 > num3:
        print(num1, "is the largest number.")
    elif num2 > num1 and num2 > num3:
        print(num2, "is the largest number.")
    elif num3 > num1 and num3 > num2:
        print(num3, "is the largest number.")
    else:    
        print("All numbers are equal.")
