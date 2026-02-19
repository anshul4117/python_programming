# 7.Write a program to check whether a character is a vowel or consonant without using inbilt (isalpha) and use only if-elif-else.
char = input("Enter a character: ") 
if char in 'aeiouAEIOU':
    print(char, "is a vowel.")
else:
    print(char, "is a consonant.")