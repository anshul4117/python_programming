# 5.Write a program to find the factorial of a number in simple way without using functions.
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} is {factorial}")