from datetime import datetime

def get_input(txt):
    return input(txt)

def time_now():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return f'{year}-{month}-{day}'

#ask yes or no and return boolean
def ask_yes_or_no(text):
    return get_input(text + ' [y/n]?: ').lower() == 'y'

