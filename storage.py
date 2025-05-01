import os
import json

#login_user
user_and_password = 'data/user_and_password.json'

def load_user_psw():
    return load_json(user_and_password)

def save_user_psw(data):
    dump_json(user_and_password, data)

#user_data
def make_user_file(username):
    return f'data/users/{username}.json'

def load_user_info(username):
    file = make_user_file(username)
    return load_json(file)

def save_user_info(username, data: str):
    file = make_user_file(username)
    dump_json(file, data)

#storage
def load_json(file):
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        return {}
    with open(file, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def dump_json(file, new_data):
    with open(file, 'w') as f:
        json.dump(new_data, f, indent=4)


