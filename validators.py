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

def is_empty_name(n):
    from login_user import get_name
    if len(n) == 0:
        print('Name cannot be empty.')
        return get_name()
    elif len(n) < 2:
        print('Name cannot be short.')
        return get_name()
    else:
        return n

def is_valid_password(p):
    from login_user import get_password
    if len(p) < 8:
        print("Password must be at least with 8 characters.")
        return get_password()
    elif not any(c.isupper() for c in p):
        print('Password must contain at least one upper case letter.')
        return get_password()
    elif not any(c.islower() for c in p):
        print("Password must contain at least one lower case letter.")
        return get_password()
    elif not any(c.isdigit() for c in p):
        print("Password must contain at least one number.")
        return get_password()
    elif not all(c.isalnum() for c in p):
        print("Password cannot contain special characters and spaces.")
        return get_password()
    else:
        return p


