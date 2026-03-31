input_str = input("Enter a string: ")

char_count = {}
for char in input_str:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

print("String:", input_str)
print("Character frequency:", char_count)