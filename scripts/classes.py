from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class History:

    def __init__(self):
        self._transactions = []


    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    
    def display_transactions(self):
        for transaction in self._transactions:
            print(transaction)

    @property
    def transactions(self):
        return self._transactions



class Customer(ABC):

    customers = []

    @classmethod
    def display_customers(cls):
        for customer in cls.customers:
            print(customer.get_info())


    def __init__(self, address, accounts):
        self._address = address
        self._accounts = accounts
        self._account_list = []
        self._num_accounts = 0

        Customer.customers.append(self)


    def add_account(self, account):
        self._accounts.append(account)
        self._num_accounts += 1
        return self._num_accounts
    
    
    def get_accounts(self):
        for account in self._accounts:
            self._account_list.append(account.number)
        return self._account_list

    
    @abstractmethod
    def get_info():
        pass



class NaturalPerson(Customer):

    @classmethod
    def find_customer(cls, cpf):
        for customer in Customer.customers:
            if cpf == customer._cpf:
                return customer

    def __init__(self, cpf, name, birth_date, address, accounts=None):
        self._cpf = cpf
        self._name = name
        self._birth_date = birth_date

        if accounts is None:
            accounts = []

        super().__init__(address=address, accounts=accounts)
        

    def get_info(self):
        return f'''
Name: {self._name}
CPF: {self._cpf}
Birth date: {self._birth_date}
Address: {self._address}
Accounts: {self.get_accounts()}'''
    
    @property
    def cpf(self):
        return self._cpf
        


class Account(ABC):

    accounts = []

    @classmethod
    def display_accounts(cls):
        for account in cls.accounts:
            print(account.get_info())


    def __init__(self, balance: float, customer_cpf: str, history: History):
        self._balance = balance
        self._agency = "0001"
        self._customer_cpf = customer_cpf
        self.history = history
        self._num_transactions = 0
        self._last_transaction_time = None
        self._customer = NaturalPerson.find_customer(customer_cpf)
        self._number = self._customer.add_account(self)

        Account.accounts.append(self)


    @property
    def balance(self):
        return self._balance
    

    @property
    def number(self):
        return self._number


    @abstractmethod
    def withdraw():
        pass


    @abstractmethod
    def deposit():
        pass
    

    @abstractmethod
    def get_info():
        pass



class CheckingAccount(Account):

    def __init__(self, balance: float, customer_cpf: str, withdraw_limit, history=None):
        self._withdraw_limit = withdraw_limit
        self._daily_limit = 10

        if history is None:
            history = History()

        super().__init__(balance, customer_cpf, history)

    
    def get_info(self):
        return f'''
Number: {self._number}
Balance: {self._balance}
Customer: {self._customer_cpf}
Daily limit: {self._daily_limit}
Withdraw limit: {self._withdraw_limit}'''
    

    def withdraw(self, value: float):
        current_time = datetime.now()

        if self._last_transaction_time is None:
            self._last_transaction_time = current_time

        if not self.transaction_available(current_time):
            return
        
        if value > self._withdraw_limit:
            print("\nWithdrawal unavailable: value surpasses withdraw limit.")
            return
        
        if value > self._balance:
            print("\nWithdrawal unavailable: insufficient balance.")
            return
        
        self._balance -= value
        self._num_transactions += 1
        self.history.add_transaction(f"Withdrawal: R$ {value:.2f} at {current_time}")

        if self._num_transactions == 1:
            self._last_transaction_time = current_time



    def deposit(self, value: float):
        current_time = datetime.now()

        if not self.transaction_available(current_time):
            return

        if value <= 0:
            print("\nYou can't deposit non-positive values.")
            return
    
        self._balance += value
        self._num_transactions += 1
        self.history.add_transaction(f"Deposit: R$ {value:.2f} at {current_time}")

        if self._num_transactions == 1:
            self._last_transaction_time = current_time


    def transaction_available(self, current_time):
        if self._num_transactions >= self._daily_limit:
            if current_time - self._last_transaction_time >= timedelta(hours=24):
                print("\n24 hours passed. Resetting transaction count.\n")
                self._num_transactions = 0
                self._last_transaction_time = current_time
                return True
            else:
                print("Deposit unavailable: you reached you daily limit.")
                return False
