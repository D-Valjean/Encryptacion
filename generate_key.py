from cryptography.fernet import Fernet
import os

# Generate a random 32-bit key
key = Fernet.generate_key()
print(key)
