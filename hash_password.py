import hashlib

password = input("Enter password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

print("\nOriginal password:")
print(password)

print("\nSHA-256 hash:")
print(hashed)
