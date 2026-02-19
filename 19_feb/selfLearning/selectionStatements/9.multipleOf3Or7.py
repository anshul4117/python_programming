# 9.Write a program to check whether a number is a multiple of 3 or 7.
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 7 == 0:
    print(number," is a multiple of both 3 and 7.")
elif number % 3 == 0:
    print(number," is a multiple of 3.")
elif number % 7 == 0:
    print(number," is a multiple of 7.")
else:    
    print(number," is not a multiple of 3 or 7.")