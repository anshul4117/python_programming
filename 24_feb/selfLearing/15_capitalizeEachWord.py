# Q15: Capitalize the first letter of each word in a string without using title()
# Input: "hello world python programming"
# Output: "Hello World Python Programming"

sentence = "hello world python programming"

words = sentence.split()
capitalized_words = []

for word in words:
    new_word = word[0].upper() + word[1:]
    capitalized_words.append(new_word)

result = " ".join(capitalized_words)

print("Original:", sentence)
print("Capitalized:", result)

# Output:
# Original: hello world python programming
# Capitalized: Hello World Python Programming
