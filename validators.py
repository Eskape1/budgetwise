import hashlib

def hash_password(psw):
    psw.encode()
    h = hashlib.new('SHA256')
    h.update(psw.encode())
    return h.hexdigest()

def is_float(balance):
    if balance == int(balance):
        return int(balance)
    return balance

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

#ask yes or no and return boolean
def yes_no_q(text):
    return input(text + ' [y/n]?: ').lower() == 'y'

