# Simple password generator

from random import choice
from string import ascii_letters


list_of_str = ascii_letters + '0123456789' + r'!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

try:
    password = ''
    passwordLength = int(input('Enter the length of the password:'))
    for i in range(passwordLength):
        pass_dig = choice(list_of_str)
        password += pass_dig
    print(password)
except:
    print('Please enter an integer !')
