# ========== XOR GUI (Password Protector) ==========
import PySimpleGUI as sg

from time import sleep
from random import choice
from string import ascii_letters
from numpy import ceil, repeat

# ========== HELPER FUNCTIONS ==========

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

# ========================================

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


# Color theme option, provided by the PySimpleGUI
sg.ChangeLookAndFeel('SandyBeach')


layout = [
            [sg.Text('Password:', font=('Verdana', 11)),
             sg.Input(),
             sg.Button('Get Size')],
            [sg.Text('Key:', font=('Verdana', 11)),
             sg.Input()],
            [sg.Button('Generate Random ASCII Key', button_color='orange'),
             sg.Text('with size', font=('Verdana', 11)),
             sg.Input(size=(15, 1), default_text=10)],
            [sg.Button('Encrypt', button_color='red'),
             sg.Button('Decrypt', button_color='blue')]
        ]

window = sg.Window('XOR Password Protector', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        password, key, keyLengthASCII = values[0], values[1], values[2]
        if event == 'Encrypt':
            encrypted_message = encryptXOR(password, key)
            # changing the format of the output
            print('Encrypting the password...')
            sleep(2)
            print('Your password has been encrypted!')
            print('Encrypted password:')
            print(encrypted_message)

        elif event == 'Decrypt':
            decrypted_message = decryptXOR(password, key)
            print('Decrypting the password...')
            sleep(2)
            print('Your password has been decrypted!')
            print('Decrypted password:')
            print(decrypted_message)

        elif event == 'Generate Random ASCII Key':
            randomKey = generateASCIIkey(int(keyLengthASCII))
            print('Generating Random ASCII Key...')
            sleep(2)
            print('A random key has been generated!')
            print(randomKey)

        elif event == 'Get Size':
            print('The size of the password is:', len(password))
