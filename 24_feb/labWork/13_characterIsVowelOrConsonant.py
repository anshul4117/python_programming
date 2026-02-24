char = input("Enter a character: ")

# Convert to lower case for easy comparison
char = char.lower() 
if(char.isalpha()):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input. Please enter a single alphabetic character.")



# Output:
# Enter a character: E
# Vowel