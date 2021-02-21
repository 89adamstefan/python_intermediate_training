from decimal import Decimal


def exercises_1():
    list_names = ["Anna", "Patrick", "Bryan", "Carl", "Jason"]
    print("Case A")

    result_a = sorted(list_names, key=lambda name: len(name))
    print(result_a)

    print("Case B")
    result_b = sorted(list_names, key=lambda name: len(name), reverse=True)
    print(result_b)

    print("Case C")
    result_c = sorted(list_names, key=lambda name: name[0])
    print(result_c)


class BankAccount():
    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Account name {self.name} balance is {self.balance}"


def exercises_2_3():
    acc_1 = BankAccount("Acc1", Decimal(1000))
    acc_2 = BankAccount("Acc2", Decimal(4000))
    acc_3 = BankAccount("Acc3", Decimal(5000))
    acc_4 = BankAccount("Acc4", Decimal(7000))
    acc_5 = BankAccount("Acc5", Decimal(10000))

    accounts_list = [acc_1, acc_2, acc_3, acc_4, acc_5]

    print("Exercise 2")

    filtered_accounts = list(filter(lambda acc: acc if acc.balance > Decimal(4500) else None, accounts_list))
    print(filtered_accounts)

    print("Exercise 3")

    max_accounts = max(accounts_list, key=lambda acc: acc.balance)
    print(max_accounts)


from random import randint


def exercises_4():
    randoms_list = [randint(0, 101) for item in range(10)]
    print("Before")
    print(randoms_list)
    print("After")
    print(list(map(lambda number: number * 2, randoms_list)))

from random import randint

def exercises_5():

    number_list = [int(randint(100, 200)) for item in range(20)]
    print("Before")
    print(number_list)
    print("Ascending sort")
    print(sorted(number_list))
    print("Descending sort")
    print(sorted(number_list, reverse=True))
