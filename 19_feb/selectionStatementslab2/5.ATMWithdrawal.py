# 5. ATM Withdrawal System
# Conditions:
# • Account balance must be sufficient
# • Daily withdrawal limit ₹50,000
# • ATM cash availability
# Display appropriate messages for each condition failure.

balance = int(input("Enter your account balance: "))
withdraw_amount = int(input("Enter withdrawal amount: "))
atm_cash = int(input("Enter ATM available cash: "))

daily_limit = 50000

if withdraw_amount > daily_limit:
    print("Withdrawal failed: Exceeds daily limit of 50000.")
else:
    if withdraw_amount > balance:
        print("Withdrawal failed: Insufficient account balance.")
    else:
        if withdraw_amount > atm_cash:
            print("Withdrawal failed: ATM does not have enough cash.")
        else:
            balance = balance - withdraw_amount
            atm_cash = atm_cash - withdraw_amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
