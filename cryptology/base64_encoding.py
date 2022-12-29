import base64


def encode_script(filePATH):
    """
    Encoding the python script into base64 for a given file path

    Args:
        filePATH [str]: The path of the python script that is
        going to be encoded
    """
    with open(filePATH, 'rb') as f:
        data = f.read()

    with open(filePATH + 'b64', 'wb') as f:
        f.write(base64.b64encode(data))


def read_script(enc_filePATH):
    """
    Reading the encoded string for the use of the exec function.
    """
    with open(enc_filePATH, 'r') as f:
        data = f.read()
        return data


filePATH = 'hello.py'           # It can be full or relative path
enc_filePATH = 'hello.pyb64'    # It can be full or relative path

# Encoding the python script
encode_script(filePATH)

# Reading the encoded python script
encrypted_script = read_script(enc_filePATH)

# Decrypting the python script
decrypted_script = base64.b64decode(encrypted_script)

# Executing the code
exec(decrypted_script)
