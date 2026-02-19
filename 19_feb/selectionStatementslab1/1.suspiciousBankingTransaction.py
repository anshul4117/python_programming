# A bank wants to flag suspicious transactions.
# • If the transaction amount is greater than ₹2,00,000
# • And the account is less than 6 months old
# • And the transaction is international
# Write a program to detect whether the transaction should be flagged for manual verification.


amount = float(input("Enter the transaction amount: "))


# if(amount > 200000 and account_age < 6 and is_international.lower() == "yes" ):
#     print("Transaction flagged for manual verification.")
# else:
#     print("amount should be greater than ₹2,00,000")


if(amount > 200000):
    account_age = int(input("Enter the account age in months: "))
    if(account_age < 6 ):
        is_international = input("Is the transaction international? (yes/no): ")
        if(is_international.lower() == "yes"):
            print("Transaction flagged for manual verification.")
        else:
            print("Transaction is not international. No flag.")
    else:
        print("account age should be less then 6 months")
else: 
    print("amount should be greater than ₹2,00,000")
