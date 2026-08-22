# Password Strength Checker
import string
from getpass import getpass


def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def main():
    password = getpass("Enter your password: ")

    strength = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")

    print("\nPassword Requirements:")
    print("- At least 8 characters")
    print("- One uppercase letter")
    print("- One lowercase letter")
    print("- One number")
    print("- One special character")


if _name_ == "_main_":
    main()
