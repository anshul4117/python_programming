string = input("Enter a string : ")


char_count = {}
for char in string:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

first_non_repeating = None
for char in string:
    if char_count[char] == 1:
        first_non_repeating = char
        break

print("String:", string)
print("First non-repeating character:", first_non_repeating)