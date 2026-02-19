# 2. Smart Login System
# Create a login system with:
# • Username validation
# • Password validation
# • Maximum 3 failed attempts
# If 3 attempts fail, lock the account.
# Predefined credentials


VALID_USERNAME = "anshul"
VALID_PASSWORD = "anshul123"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == VALID_USERNAME:
        if password == VALID_PASSWORD:
            print("Login successful!")
            break
        else:
            attempts = attempts + 1
            print("Wrong password.")
    else:
        attempts = attempts + 1
        print("Wrong username.")

    if attempts < 3:
        print("Attempts left:", 3 - attempts)
    else:
        print("Account locked. Too many failed attempts.")
