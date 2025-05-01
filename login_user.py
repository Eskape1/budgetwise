from validators import *
from storage import *

#the dictionary with users and them hash
user_psw = load_json(user_and_password)

#saves username and password in text file
def save_new_user(name, password):
    user_psw[name] = password

def get_name():
    name = input('Enter your name: ')
    return name

def get_password():
    psw = input('Enter your password: ')
    return psw

#check current hash with the hash from database
def check_hash(old, new):
    if new != old:
        print('Wrong password')
        return True
    else:
        return False

def registration(name):
    psw = get_password()
    while not is_valid_password(psw):
        psw = get_password()
    psw = hash_password(psw + name)
    save_new_user(name, psw)
    psw2 = hash_password(input('Confirm your password: ') + name)
    while check_hash(psw,psw2):
        psw2 = hash_password(input('Confirm your password: ') + name)
        check_hash(psw,psw2)
    dump_json(user_and_password, user_psw)
    return name

def login(name):
    psw = get_password()
    psw = hash_password(psw + name)
    while check_hash(user_psw[name],psw):
        psw = hash_password(input('Enter your password: ') + name)
        check_hash(user_psw[name],psw)
    return name

def session():
    name = get_name()
    check_user_in_data(name)
    return name



def check_user_in_data(name):
    if name in user_psw.keys():
        if yes_no_q('Do you want to login'):
            login(name)
        else:
            session()
    else:
        if yes_no_q('Do you want to registrate'):
            registration(name)
        else:
            session()


if __name__ == '__main__':
    pass