import random 

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~@#$%^&*()_-+=;:,.><?/'

total_password = input('Enter Total Password To Generate: ')
total_password = int(total_password)

password_length = input('Enter Password Length: ')
password_length = int(password_length)

for i in range(total_password):
    passwords = ''
    for c in range(password_length):
        passwords += random.choice(characters)
    print(passwords)
