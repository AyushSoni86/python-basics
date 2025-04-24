password = input("Enter a password: \n")


if len(password) < 6:
    password_strength = "Weak"  
elif len(password) <= 10:
    password_strength = "Meduim"
else:
    password_strength = "Strong"

print(password_strength)