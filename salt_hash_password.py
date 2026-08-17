import os
import hashlib

password = input("Enter password: ")

salt = os.urandom(16)

hashed = hashlib.sha256(salt + password.encode()).hexdigest()

print("Salt:", salt.hex())
print("Hash:", hashed)
