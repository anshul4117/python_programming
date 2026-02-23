numbers_input = input("Enter numbers separated by space: ")

values = numbers_input.split()
numbers = []

for v in values:
    numbers.append(int(v))

unique_numbers = set(numbers)

print("Unique Numbers:", unique_numbers)