# Loan approval depends on:
# • Credit score
# • Monthly income
# • Existing loan amount
# Rules:
# • Credit score < 600 → Reject
# • 600–750 → Further check income
# • 750 → Approve
# If income < ₹30,000 and existing loans > ₹5,00,000 → Reject.


credit_score = int(input("Enter credit score: "))
monthly_income = int(input("Enter monthly income: "))
existing_loans = int(input("Enter existing loan amount: "))

if credit_score < 600:
    print("Loan Rejected: Credit score too low")
elif credit_score <= 750:
    if monthly_income < 30000 and existing_loans > 500000:
        print("Loan Rejected: Income too low and existing loans too high")
    else:
        print("Loan Approved")
else:
    print("Loan Approved")