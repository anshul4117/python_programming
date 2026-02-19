# 3.Write a program to multiply two numbers.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if(num1 == 0 or num2 == 0):
    print("The product of two numbers is: 0")
else:    
    product = num1 * num2
    print("The product of two numbers is: ", product)
