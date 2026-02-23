basic_salary = 25000
bonus = 5000

if basic_salary > 0:
    hra = (20 * basic_salary) / 100
    total_salary = basic_salary + hra + bonus

    print("HRA:", hra)
    print("Total Monthly Salary:", total_salary)
else:
    print("Invalid basic salary")

# output
# HRA: 5000.0
# Total Monthly Salary: 35000.0  
