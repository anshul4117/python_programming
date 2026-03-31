
numbers = [45, 23, 89, 12, 67, 34, 89, 56]


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