# Problem 10
# Problem Statement: Reverse a given number.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

number = int(input("Enter a number : "))
orgNum = number
rev = 0
while number > 0:
    rem = number % 10 
    rev = rev * 10 + rem
    number = number // 10

print("Orignal Number is : ", orgNum)
print("Reverse of the Number is : ", rev)

# output
# Enter a number : 311
# Orignal Number is :  311
# Reverse of the Number is :  113