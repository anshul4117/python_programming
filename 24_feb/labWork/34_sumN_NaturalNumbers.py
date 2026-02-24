# Problem 34
# Problem Statement: Find sum of first N natural numbers.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

num = int(input("Enter a number : "))
totalSum = 0
for i in range(1, num+1):
    totalSum = totalSum + i
print("Sum of first ", num, " natural numbers is : ", totalSum)