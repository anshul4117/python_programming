s = set()

n = int(input("How many elements? "))

for i in range(n):
    value = input("Enter element: ")
    s.add(value)      # using add() method

print("Set:", s)