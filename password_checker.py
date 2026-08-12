import string
from getpass import getpass
password= getpass("Enter your password: ")

password = input("Enter your password: ")

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
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

print("\nPassword Requirements:")
print("- At least 8 characters")
print("- One uppercase letter")
print("- One lowercase letter")
print("- One number")
print("- One special character")


