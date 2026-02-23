set1 = set(input("Enter first set: ").split())
set2 = set(input("Enter second set: ").split())

result = set1.difference(set2)

print("Difference (Set1 - Set2):", result)