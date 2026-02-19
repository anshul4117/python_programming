# 6.Write a program to check whether a number is divisible by 5 and 11.
num = int(input("Enter a number: "))

if(num <= 0):
    print("number should be positive and greater than zero")
else:
    if(num % 5 == 0 and num % 11 == 0):
        print("The number is divisible by 5 and 11")
    else:
        print("The number is not divisible by 5 and 11")
