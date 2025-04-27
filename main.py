import json

from login_user import session, yes_no_q, load_json
from datetime import datetime

class Session:
    __username = session()
    file = f'data/{__username}.json'
    budget_data = load_json(file)

    def check_new_user(self):
        if self.budget_data == {}:
            self.budget_data.setdefault('Balance', 0)
            self.budget_data.setdefault('Incomes', [])
            self.budget_data.setdefault('Expenses', [])

    @staticmethod
    def time_now():
        now = datetime.now()

        year = now.year
        month = now.month
        day = now.day
        return f'{year}-{month}-{day}'

    def dump_json(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(self.budget_data, f, indent=1)


class Balance(Session):

    def __init__(self):
        self.balance = self.budget_data['Balance']
        self.incomes = self.budget_data['Incomes']
        self.expenses = self.budget_data['Expenses']


    def view_balance(self):
        print(f'Your balance: {self.balance}')

    def add_money(self):
        money = int(input('How many will you add: '))
        time = self.time_now()
        self.balance += money
        return money, time

    def take_money(self):
        money = int(input('How many will you take: '))
        time = self.time_now()
        self.balance -= money
        return money, time



class Menu(Balance):


    @staticmethod
    def print_menu():
        print('1. View balance\n2. Add money\n3. Take money\n4. Logg out\n5. Quit')
        return input('Enter a number: ')


    def main_menu(self, choice):
        match choice:
            case '1':
                self.view_balance()
            case '2':
                amount, time = self.add_money()
                self.balance = self.balance
                self.incomes.append({'amount':amount, 'date': time})
            case '3':
                amount, time = self.take_money()
                self.balance = self.balance
                self.expenses.append({'amount': amount, 'date': time})
            case '4':
                if yes_no_q('Are you sure you want to logg out'):
                    pass

            case '5':
                if yes_no_q('Do you want to save new changes'):
                    self.dump_json()
                if yes_no_q('Are you sure you want to exit'):
                    quit()

            case _:
                print('Wrong command.')
        self.main_menu(self.print_menu())

if __name__ == '__main__':
    user = Session()
    user.check_new_user()
    user_menu = Menu()
    c = user_menu.print_menu()
    user_menu.main_menu(c)
    user.dump_json()
















