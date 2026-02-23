sentence = input("Enter a sentence: ")

words = sentence.split()
unique_words = set(words)

print("Unique Words:", unique_words)
print("Total Unique Words:", len(unique_words))