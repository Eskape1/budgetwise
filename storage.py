import os
import json

user_and_password = 'data/user_and_password.json'

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

