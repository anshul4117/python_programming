# Q2: Count the number of vowels and consonants in a string
# Input: "Hello World"
# Output: Vowels: 3, Consonants: 7

text = "Hello World"

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("String:", text)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# Output:
# String: Hello World
# Vowels: 3
# Consonants: 7
