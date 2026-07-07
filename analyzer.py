import re

def analyze_password(password, common_passwords):

    score = 0
    suggestions = []

    result = {
        "length" : False,
        "uppercase" : False,
        "lowercase" : False,
        "number" : False,
        "special" : False,
        "common" : False,
        "repeat" : False,
    }

    if len(password) >= 8:
        result["length"] = True
        score += 20
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        result["uppercase"] = True
        score += 15
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        result["lowercase"] = True
        score += 15
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        result["number"] = True
        score += 15
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result["special"] = True
        score += 20
    else:
        suggestions.append("Add special characters.")

    if password.lower() not in common_passwords:
        result["common"] = True
        score += 10
    else:
        suggestions.append("Avoid common passwords.")

    if not re.search(r"(.)\1{2,}", password):
        result["repeat"] = True
        score += 5
    else:
        suggestions.append("Avoid repeated characters.")

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    elif score < 90:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return score, strength, result, suggestions
