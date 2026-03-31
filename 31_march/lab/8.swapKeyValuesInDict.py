original_dict = {"name": "Alice", "age": "25", "city": "New York"}

swapped_dict = {}

for key, value in original_dict.items():
    swapped_dict[value] = key

print("Original dictionary:", original_dict)
print("Swapped dictionary:", swapped_dict)