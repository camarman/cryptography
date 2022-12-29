from math import ceil
from random import choice
from string import ascii_letters

from numpy import repeat

#---------- HELPER FUNCTIONS ----------#


def resizeKey(asciiArr_message, asciiArr_key):
    """
    Resizing the length of the key, in order to perform XOR operations easily.

    Args:
        asciiArr_message [str]: An array the consist of ASCII codes, for a given messages
        asciiArr_key [str]: An array the consist of ASCII codes, for a given key
    """
    messageLength = len(asciiArr_message)
    keyLength = len(asciiArr_key)
    r = ceil(messageLength/keyLength)
    resize_binArray_key = repeat(asciiArr_key, r)
    resize_binArray_key = resize_binArray_key[:messageLength]
    return resize_binArray_key


def generateASCIIkey(keyLengthASCII):
    """
    Generating random printable ascii key

    Args:
        keyLengthASCII [int]: The desired length of the ASCII key
    """
    randomKey = ''
    ascii_extended = ascii_letters + '0123456789' + \
        r'!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    for i in range(keyLengthASCII):
        randomKey += choice(ascii_extended)
    return randomKey


def format_output(encrypted_message):
    return ','.join([str(i)[2:] for i in encrypted_message])

#----------------------------#

def encryptXOR(message, key):
    """
    Encrypting the message for a given key

    Args:
        message [str]: The input message that is going to be encrypted
        key [str]: The key that generated randomly, or entered by the user

    Returns:
        Encrypted message
    """
    binArray_message = [ord(char) for char in message]
    binArrray_key = [ord(char) for char in key]
    binArrray_key = resizeKey(binArray_message, binArrray_key)
    # performing the XOR operation
    encrypted_message = [hex(i ^ j) for (i, j) in list(
        zip(binArray_message, binArrray_key))]
    return format_output(encrypted_message)


def decryptXOR(encrypted_message, key):
    """
    Decrypting the message for a given key

    Args:
        encrypted_message [str]: The encrypted message
        key [str]: The key that generated randomly, or entered by the user

    Returns:
        Decrypted message
    """
    encrypted_message = [int('0x'+i, 0) for i in encrypted_message.split(',')]
    binArrray_key = [ord(char) for char in key]
    binArrray_key = resizeKey(encrypted_message, binArrray_key)
    # performing the XOR operation
    decrypted_message = ''.join(
        [chr(i ^ j) for (i, j) in list(zip(encrypted_message, binArrray_key))])
    return decrypted_message
