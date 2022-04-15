import base64

# The code goes here

code = b""
print('Hello, World!')
""

# Encrypting the code in base64
encrypted_script = base64.b64encode(code)

# Decrypting the code in base64
decrypted_script = base64.b64decode(encrypted_script)

# Executing the code
exec(decrypted_script)
