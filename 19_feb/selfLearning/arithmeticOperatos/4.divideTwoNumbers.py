# 4.Write a program to divide two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 != 0:
    result = num1 / num2
    print("The result of division is:", result)
else:    
    print("num2 cannot be zero")