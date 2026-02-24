# Problem 14
# Problem Statement: Check whether a character is digit or alphabet.
# Input Format: Read input from standard input.
# Output Format: Print the required output.
# Constraints: Standard constraints apply.

ch = input("Enter something: ")
if(ch.isalpha()):
    print("Alphabet")
elif(ch.isdigit()):
    print("Digit")
elif(ch.isalnum()):
    print("character is alphanumeric")
else:
    print("Special Character")

# Output:
# Enter something: 5
# Digit