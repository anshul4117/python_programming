numbers = input("Enter numbers: ").split()

count = {}

for n in numbers:
    if n in count:
        count[n] = count[n] + 1
    else:
        count[n] = 1

print("Frequency:", count)