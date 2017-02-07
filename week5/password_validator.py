def valid_password(password):
    return len(password) >= 8 and password.isalnum() and password != password.lower() and password != password.upper()

if __name__ == '__main__':
    pwd = input('Enter password: ')

    if valid_password(pwd):
        print('Passowrd is a-okay!')
    else:
        print('Password is not so good.')