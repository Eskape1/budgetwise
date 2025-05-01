from login_user import *



class User:

    def __init__(self):
        self.username = session()
        self.user_info = f'data/users/{self.username}.json'
        self.budget_data = load_json(self.user_info)
        self.check_new_user()
        self.balance = self.budget_data['Balance']
        self.incomes = self.budget_data['Incomes']
        self.expenses = self.budget_data['Expenses']
        dump_json(self.user_info, self.budget_data)


    def check_new_user(self):
        if self.budget_data == {}:
            self.budget_data.setdefault('Balance', 0)
            self.budget_data.setdefault('Incomes', [])
            self.budget_data.setdefault('Expenses', [])

    def get_user_data(self):
        return self.user_info


def user_name():
    return User()


if __name__ == '__main__':
    pass


