# Program to find common elements between two sets

set1 = set(input("Enter first set numbers: ").split())
set2 = set(input("Enter second set numbers: ").split())

common = set1.intersection(set2)

print("Common Elements:", common)