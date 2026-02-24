# Problem 8
# Problem Statement: Check whether a number is even or odd without modulus operator.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.


number = int(input("Enter a number : "))
num = (number // 2) * 2

if(num == number):
    print("Number is Even")
else :
    print("Number is Odd")

# output
# Enter a number : 213
# Number is Odd