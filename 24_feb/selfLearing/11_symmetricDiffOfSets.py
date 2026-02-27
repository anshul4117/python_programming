# Q11: Find the elements that are in one set but not the other (Symmetric Difference)
# Input: set1 = {1, 2, 3, 4}, set2 = {3, 4, 5, 6}
# Output: {1, 2, 5, 6}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

only_in_set1 = set1 - set2
only_in_set2 = set2 - set1
sym_diff = set1.symmetric_difference(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Only in Set 1:", only_in_set1)
print("Only in Set 2:", only_in_set2)
print("Symmetric Difference:", sym_diff)

# Output:
# Set 1: {1, 2, 3, 4}
# Set 2: {3, 4, 5, 6}
# Only in Set 1: {1, 2}
# Only in Set 2: {5, 6}
# Symmetric Difference: {1, 2, 5, 6}
