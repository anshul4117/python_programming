# Q5: Find the second largest number in a list without using sort
# Input: [12, 45, 7, 23, 56, 34]
# Output: 45

numbers = [12, 45, 7, 23, 56, 34]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("List:", numbers)
print("Largest:", largest)
print("Second Largest:", second_largest)

# Output:
# List: [12, 45, 7, 23, 56, 34]
# Largest: 56
# Second Largest: 45
