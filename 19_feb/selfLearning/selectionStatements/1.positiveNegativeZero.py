# 1.Write a program to check whether a number is positive, negative, or zero.

number = int(input("Enter a Number : "))
if(number > 0):
    print("Positive")
else:
    if(number < 0):
        print("Negative")
    else:
        print("Zero")
