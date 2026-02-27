# Q12: Replace all occurrences of a substring in a string
# Input: "I like cats. cats are cute. I have two cats."
# Replace "cats" with "dogs"
# Output: "I like dogs. dogs are cute. I have two dogs."

sentence = "I like cats. cats are cute. I have two cats."
old_word = "cats"
new_word = "dogs"

result = sentence.replace(old_word, new_word)

print("Original:", sentence)
print("After Replace:", result)

# Output:
# Original: I like cats. cats are cute. I have two cats.
# After Replace: I like dogs. dogs are cute. I have two dogs.
