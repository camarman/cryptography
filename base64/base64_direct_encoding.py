import base64

code = b""
print('Hello, World!')
""

# Encrypting the code via base64
encrypted_message = base64.b64encode(code)

# Decrypting the code via base64
decrypted_message = base64.b64decode(encrypted_message)

# Executing the code
exec(decrypted_message)
