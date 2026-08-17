common_passwords = [
    "123456",
    "password",
    "qwerty",
    "admin",
    "welcome123"
]

user_password = input("Enter password: ")

if user_password in common_passwords:
    print("❌ Weak password detected")
else:
    print("✅ Password not found in common weak password list")
