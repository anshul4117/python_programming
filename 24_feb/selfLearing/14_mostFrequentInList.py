# Q14: Find the most frequent element in a list
# Input: [3, 1, 2, 3, 4, 3, 2, 1, 3]
# Output: Most frequent element is 3 (appears 4 times)

numbers = [3, 1, 2, 3, 4, 3, 2, 1, 3]

freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_element = None
max_count = 0
for key, value in freq.items():
    if value > max_count:
        max_count = value
        max_element = key

print("List:", numbers)
print("Frequency:", freq)
print(f"Most Frequent Element: {max_element} (appears {max_count} times)")

# Output:
# List: [3, 1, 2, 3, 4, 3, 2, 1, 3]
# Frequency: {3: 4, 1: 2, 2: 2, 4: 1}
# Most Frequent Element: 3 (appears 4 times)
