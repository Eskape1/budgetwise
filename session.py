from def_library import *
from validators import is_float
from user_data import User
from def_library import get_input
from storage import save_user_info


class Balance(User):

    def view_balance(self):
        print(f'Your balance: {is_float(self.balance)}')

    def handle_transaction(self, txt: str, is_income: bool):
        amount = float(get_input(txt))
        self.balance += amount if is_income else -amount
        return amount

    def record_transaction(self, amount: float, is_income: bool):
        self.budget_data['Balance'] = is_float(self.balance)
        entry = {'amount': amount, 'date': time_now()}
        if is_income:
            self.incomes.append(entry)
        else:
            self.expenses.append(entry)


class Menu(Balance):

    def save_changes(self):
        if ask_yes_or_no('Do you want to save new changes'):
            save_user_info(self.username, self.budget_data)

    @staticmethod
    def print_menu():
        print('1. View balance\n2. Add money\n3. Take money\n4. Logg out\n5. Quit')
        return get_input('Enter a number: ')


    def main_menu(self, choice):
        match choice:
            case '1':
                self.view_balance()
            case '2':
                amount = self.handle_transaction('How many will you add: ', True)
                self.record_transaction(amount, True)
            case '3':
                amount = self.handle_transaction('How many will you take: ', False)
                self.record_transaction(amount, False)
            case '4':
                self.save_changes()
                if ask_yes_or_no('Are you sure you want to logg out'):
                    from main import main
                    print('You logged out!')
                    main()
            case '5':
                self.save_changes()
                if ask_yes_or_no('Are you sure you want to exit'):
                    quit()
            case _:
                print('Wrong command.')
        self.main_menu(self.print_menu())

if __name__ == '__main__':
    pass

















