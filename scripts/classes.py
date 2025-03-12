from abc import ABC, abstractmethod

class Customer:

    def __init__(self, address, accounts):
        self._address = address
        self._accounts = accounts

    def make_transaction(account, transaction):
        pass

    def add_account(account):
        pass


class Account():

    def __init__(self, account_id, balance, agency, customer, history):
        self._id = account_id
        self._balance = balance
        self._agency = agency
        self._customer = customer
        self._history = history

    def balance() -> float:
        pass
    
    def new_account(self, customer):
        pass

    def withdraw(value: float) -> bool:
        pass

    def deposit(value: float) -> bool:
        pass


class Transaction(ABC):

    @abstractmethod
    def record(account):
        pass


class History:

    def add_transaction(transaction):
        pass


class NaturalPerson(Customer):

    def __init__(self, cpf, name, birth_date):
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date


class CheckingAccount(Account):

    def __init__(self, limit, withdraw_limit):
        self._limit = limit
        self._withdraw_limit = withdraw_limit


class Deposit(Transaction):

    def __init__(self, value):
        self._value = value

    def record():
        pass


class Withdrawal(Transaction):

    def __init__(self, value):
        self._value = value

    def record():
        pass
