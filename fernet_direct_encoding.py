from cryptography.fernet import Fernet

code = b""
print('Hello, World!')
""

key = Fernet.generate_key()
encryption_type = Fernet(key)

# Encrypting the code via Fernet
encrypted_message = encryption_type.encrypt(code)

# Decrypting the code via Fernet
decrypted_message = encryption_type.decrypt(encrypted_message)

# Executing the code
exec(decrypted_message)
