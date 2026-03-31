numbers = int(input("Enteer a list of the numbers : ").split())
target = int(input("Enter your target value :"))

pairs = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            pairs.append((numbers[i], numbers[j]))

print("List:", numbers)
print("Target:", target)
print("Pairs with target sum:", pairs)