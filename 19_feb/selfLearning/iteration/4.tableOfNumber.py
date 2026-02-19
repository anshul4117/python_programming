# 4.Write a program to print the multiplication table of a given number without format string in simple way.

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "*", i, "=", num * i)
