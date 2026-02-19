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
