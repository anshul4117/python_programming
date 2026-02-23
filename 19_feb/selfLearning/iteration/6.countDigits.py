# 6.Write a program to count the number of digits in a number .
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n //= 10
    count += 1
print("Number of digits: ",count)

# output
# Enter a number: 12345
# Number of digits:  5
