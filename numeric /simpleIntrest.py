def calculate_simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Values cannot be negative.")

    return (principal * rate * time) / 100


try:
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time (in years): "))

    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest is: {si:.2f}")

except ValueError as e:
    print("Error:", e)
    