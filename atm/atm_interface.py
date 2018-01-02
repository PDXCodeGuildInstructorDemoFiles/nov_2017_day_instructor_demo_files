import csv


class Account:
    def __init__(self, starting_balance, type):
        self.balance = starting_balance
        self.account_type = type

    def get_funds(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            raise ValueError
        self.balance -= amount
        return self.balance

    def check_withdraw(self, amount):
        return self.balance - amount > 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def get_standing(self):
        return self.balance >= 1000

    # def from_csv_string(self, record):
    #     spamreader = csv.reader(record, delimiter=',', quotechar='|')
    #     for i in spamreader:
    #         print(i)


if __name__ == "__main__":
    tmp = Account(500, 'checking')
    record = '5902692944186857,151.5,checking'
    # tmp.from_csv_string([record])
