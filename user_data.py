from login_user import session
from storage import make_user_file, load_user_info, save_user_info


class User:

    def __init__(self):
        self.username = session()
        self.user_file = make_user_file(self.username)
        self.budget_data = load_user_info(self.username)
        self.check_new_user()
        self.balance = self.budget_data['Balance']
        self.incomes = self.budget_data['Incomes']
        self.expenses = self.budget_data['Expenses']
        save_user_info(self.username, self.budget_data)


    def check_new_user(self):
        if self.budget_data == {}:
            self.budget_data.setdefault('Balance', 0)
            self.budget_data.setdefault('Incomes', [])
            self.budget_data.setdefault('Expenses', [])

    def get_user_data(self):
        return self.user_file

def user_name():
    return User()

if __name__ == '__main__':
    m = user_name()




