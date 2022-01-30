import random

print('==================== Password Generator ============================\n')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?1234567890'


num = int(input('How many password to generate: '))

length = int(input('Amount of passwords to generate: '))


for password in range(num):
    password = ''
    for c in range(length):
        password+= random.choice(chars)
    print('Your Password: ' + password)
