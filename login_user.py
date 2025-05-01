from validators import *
from storage import load_user_psw, save_user_psw
from def_library import get_input, ask_yes_or_no

#the dictionary with users and them hash
user_psw = load_user_psw()


def get_name():
    return is_empty_name(get_input('Enter your name: '))

def get_password():
    return get_input('Enter your password: ')

#saves username and password in text file
def save_new_user(name, password):
    user_psw[name] = password
    save_user_psw(user_psw)

#check current hash with the hash from database
def check_hash(from_file, current):
    if current != from_file:
        print('Wrong password.')
        return False
    return True


def login(name):
    while True:
        psw = get_password()
        hashed = hash_password(psw + name)
        if check_hash(user_psw[name], hashed):
            return name


def registration(name):
    psw = is_valid_password(get_password())
    hashed = hash_password(psw + name)
    save_new_user(name, hashed)

    while True:
        psw2 = get_input("Confirm your password: ")
        if check_hash(hashed, hash_password(psw2 + name)):
            break
    return name


def session():
    name = get_name()
    check_user_in_data(name)
    return name


def check_user_in_data(name):
    if name in user_psw.keys():
        if ask_yes_or_no('Do you want to login'):
            login(name)
        else:
            session()
    else:
        if ask_yes_or_no('Do you want to registrate'):
            registration(name)
        else:
            session()


if __name__ == '__main__':
    session()


