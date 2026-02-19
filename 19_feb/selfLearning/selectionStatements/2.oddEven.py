# 2.Write a program to check whether a number is even or odd.

number = int(input("Enter a Number : "))
if(number > 0):
    if(number%2 == 0):
        print("Even Number")
    else:
        print("Odd NUmber")
else:
    print("Number should be positive and greater then Zero")