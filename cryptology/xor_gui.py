from time import sleep
import PySimpleGUI as sg
from xor_encryption import *


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

window = sg.Window('XOR Password Encryption', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        password, key, keyLengthASCII = values[0], values[1], values[2]
        if event == 'Encrypt':
            encrypted_message = encryptXOR(password, key)
            # changing the format of the output
            print('Encrypting the message...')
            sleep(2)
            print('Your Message has been encrypted!')
            print('Encrypted Message:')
            print(encrypted_message)

        elif event == 'Decrypt':
            decrypted_message = decryptXOR(password, key)
            print('Decrypting the message...')
            sleep(2)
            print('Your Message has been decrypted!')
            print('Decrypted Message:')
            print(decrypted_message)

        elif event == 'Generate Random ASCII Key':
            randomKey = generateASCIIkey(int(keyLengthASCII))
            print('Generating Random ASCII Key...')
            sleep(2)
            print('A random key has been generated!')
            print(randomKey)

        elif event == 'Get Size':
            print('The size of the password is:', len(password))
