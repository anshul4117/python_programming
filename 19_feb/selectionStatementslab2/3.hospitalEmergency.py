# 3. Hospital Emergency Triage
# Patients are categorized as:
# • Critical (heart rate abnormal OR severe injury)
# • Moderate
# • Normal
# If age > 65 and condition is moderate → Upgrade priority.
# Get patient information

age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate: "))
severe_input = input("Is there severe injury? (yes/no): ")
condition = input("Enter condition (normal/moderate/critical): ")

severe_input = severe_input.lower()
condition = condition.lower()


if severe_input == "yes":
    severe_injury = True
else:
    severe_injury = False

if heart_rate < 60 or heart_rate > 100 or severe_injury == True:
    priority = "Critical"
else:
    if age > 65:
        if condition == "moderate":
            priority = "Moderate (Upgraded)"
        else:
            if condition == "critical":
                priority = "Critical"
            else:
                if condition == "moderate":
                    priority = "Moderate"
                else:
                    priority = "Normal"
    else:
        if condition == "critical":
            priority = "Critical"
        else:
            if condition == "moderate":
                priority = "Moderate"
            else:
                priority = "Normal"

print("Patient Priority:", priority)
