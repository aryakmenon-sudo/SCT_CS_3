import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.\n"

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "Add at least one uppercase letter.\n"

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "Add at least one lowercase letter.\n"

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "Add at least one number.\n"

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "Add at least one special character.\n"

    # Strength result
    if strength == 5:
        return "Strong Password 💪", remarks
    elif strength >= 3:
        return "Moderate Password ⚠️", remarks
    else:
        return "Weak Password ❌", remarks


# User input
password = input("Enter your password: ")

result, suggestions = check_password_strength(password)

print("\nResult:", result)
if suggestions:
    print("Suggestions:")
    print(suggestions)
