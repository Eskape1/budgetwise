import json
import os
import hashlib

file = 'data/user_and_password.json'

def hash_password(psw):
    psw.encode()
    h = hashlib.new('SHA256')
    h.update(psw.encode())
    return h.hexdigest()


def load_json(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return {}
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

data = load_json(file)

def dump_json(new_data):
    with open(file, 'w') as f:
        json.dump(new_data, f, indent=4)

#ask yes or no and return boolean
def yes_no_q(text):
    return input(text + ' [y/n]?: ').lower() == 'y'

# Return true if username is already exists

def exist_such_a_user(name):
    return name in data.keys()

def is_valid_password(p):
    if len(p) < 8:
        print("Password must be at least with 8 characters.")
        return False
    elif not any(c.isupper() for c in p):
        print('Password must contain at least one upper case letter.')
        return False
    elif not any(c.islower() for c in p):
        print("Password must contain at least one lower case letter.")
        return False
    elif not any(c.isdigit() for c in p):
        print("Password must contain at least one number.")
        return False
    elif not all(c.isalnum() for c in p):
        print("Password cannot contain special characters and spaces.")
        return False
    else:
        return True

#check current password with the password from database
def check_password(old, new):
    count = 0
    while True:
        if count == 4:
            print('Error "code 4300", too many attempts.\nTry again later.')
            quit()
        if new != old:
            count += 1
            print('Wrong password')
            new = input('Repeat your password: ')
        else:
            break

#saves username and password in text file

def save_new_user(name, password):
    data[name] = hash_password(password)

def registration():
    name = input('Enter your name: ')
    if exist_such_a_user(name):
        print('This name is taken')
        return login() if yes_no_q('Do you want to login') else registration()
    psw = input('Enter your password: ') + name #name is salt here

    while not is_valid_password(psw):
        psw = input('Enter your password: ') + name
    save_new_user(name, psw)
    psw = hash_password(psw)
    psw2 = hash_password(input('Confirm your password: ') + name)
    check_password(psw,psw2)
    return name

def login():
    name = input('Enter your name: ')
    if not exist_such_a_user(name):
        print('Such a user does not exist')
        return registration() if yes_no_q('Do you want to registrate') else login()
    psw = input('Enter your password: ')
    check_password(data[name], psw)
    return name

def session():
    question = yes_no_q('Are you new here')
    user = registration() if question else login()
    print('Welcome, ' + user + '!')
    dump_json(data)
    return user


if __name__ == '__main__':
    session()