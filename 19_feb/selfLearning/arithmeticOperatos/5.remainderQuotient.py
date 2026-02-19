# 5.Write a program to find remainder and quotient using operators.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if(num2 != 0):
    quotient = num1 // num2
    remainder = num1 % num2
    print("Quotient: ", quotient)
    print("Remainder: ", remainder)