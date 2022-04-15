from cryptography.fernet import Fernet

code = b""
print('Hello, World!')
""

key = Fernet.generate_key()
encryption_type = Fernet(key)

# Encrypting the code
encrypted_message = encryption_type.encrypt(code)

# Decrypting the code in base64
decrypted_message = encryption_type.decrypt(encrypted_message)

# Executing the code
exec(decrypted_message)
