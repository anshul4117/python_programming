
numbers = int(input("Enter a list of numbers: ")).split()


largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

second_largest = numbers[0]
for num in numbers:
    if num > second_largest and num != largest:
        second_largest = num

print("List:", numbers)
print("Largest element:", largest)
print("Second largest element:", second_largest)