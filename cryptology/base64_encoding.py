import base64


def encrypt_script(filePATH):
    """
    Encrypting the python script with base64 for a given file path

    Args:
        filePATH [str]: The path of the python script that is
        going to be encrypted
    """
    with open(filePATH, 'rb') as f:
        data = f.read()

    with open(filePATH + 'b64', 'wb') as f:
        f.write(base64.b64encode(data))


def read_script(enc_filePATH):
    """
    Reading the binary script for the use of the exec function.
    """
    with open(enc_filePATH, 'r') as f:
        data = f.read()
        return data


filePATH = 'hello.py'           # It can be full or relative path
enc_filePATH = 'hello.pyb64'    # It can be full or relative path

# Encrypting the python script
encrypt_script(filePATH)

# Reading the encrypted python script
encrypted_script = read_script(enc_filePATH)

# Decrypting the python script
decrypted_script = base64.b64decode(encrypted_script)

# Executing the code
exec(decrypted_script)
