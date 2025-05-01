from login_user import *
from datetime import datetime
from validators import is_float
from user_data import User






def time_now():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    return f'{year}-{month}-{day}'

class Balance(User):

    def view_balance(self):
        print(f'Your balance: {is_float(self.balance)}')

    def add_money(self):
        money = float(input('How many will you add: '))
        time = time_now()
        self.balance += money
        return money, time

    def take_money(self):
        money = float(input('How many will you take: '))
        time = time_now()
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
                self.budget_data['Balance'] = self.balance
                self.incomes.append({'amount':amount, 'date': time})
            case '3':
                amount, time = self.take_money()
                self.budget_data['Balance'] = is_float(self.balance)
                self.expenses.append({'amount': amount, 'date': time})
            case '4':
                if yes_no_q('Do you want to save new changes'):
                    dump_json(self.user_info, self.budget_data)
                if yes_no_q('Are you sure you want to logg out'):
                    from main import main
                    print('You logged out!')
                    main()
            case '5':
                if yes_no_q('Do you want to save new changes'):
                    dump_json(self.user_info, self.budget_data)
                if yes_no_q('Are you sure you want to exit'):
                    quit()
            case _:
                print('Wrong command.')
        self.main_menu(self.print_menu())

if __name__ == '__main__':
    pass















