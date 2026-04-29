import re
'''re means Regular Expressions.
It is used to search patterns inside text.'''
def check_password_strength(password):

    score = 0 #counts how many conditions are satisfied by the password
    remarks = []# stores suggestions for improving the password if it is weak or medium 

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters")
    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters")
    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters")

    # Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add numbers")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        remarks.append("Add special characters")

    # Strength Result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
      strength = "Strong"
    return strength, remarks
password = input("Enter password: ")

strength, remarks = check_password_strength(password)
    
print("Password Strength:", strength)

if remarks:
    print("Suggestions:")
    for remark in remarks:
        print("-", remark)
    