# 10.Write a program to print the Fibonacci series up to n terms.
n = int(input("Enter the number of terms: "))
a = 1
b = 0

count = 0
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence up to", n, "terms:")
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1


# output
# Enter the number of terms: 10
# Fibonacci sequence up to 10 terms:
# 1
# 0
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34    
