from time import sleep
from classes import *

def main():
    while True:
        print('''
    Choose an action:
    [1] Register
    [2] Create account
    [3] Withdraw
    [4] Deposit
    [5] View statement
    [6] View user information
    [7] View account information
    [8] Quit

    Insert the number that corresponds to the desired action:
    ''', end="")

        while True:
            try: 
                option = int(input("-> "))
                if not (option >= 1 and option <= 8):
                    print("Please, enter a valid option.")
                else:
                    break
            except ValueError:
                print("Please, enter a number.")

        match option:
            case 1: # register
                customer_creation()
            case 2: # create account
                account_creation()
            case 3: # withdraw
                withdraw_operation()
            case 4: # deposit
                deposit_operation()
            case 5: # view statement
                display_statement()
            case 6: # view user info
                Customer.display_customers()
            case 7: # view account info
                Account.display_accounts()
            case 8: # quit
                print("\nBye!\n")
                break

    
def customer_creation():
    cpf = ""
    name = ""
    birth_date = ""
    address = ""

    while True:
        valid_cpf = True
        cpf = input("\nEnter your 11-digit CPF: ")
        for customer in Customer.customers:
            if cpf == customer.cpf:
                print("\nThis CPF has already been registered.")
                valid_cpf = False

        if not(len(cpf) == 11 and cpf.isnumeric):
            print("\nEnter a valid CPF.")
            valid_cpf = False
        
        if valid_cpf:
            break

    name = input("\nEnter your name: ")

    while True:
        birth_date_str = input("\nEnter your birth date (DD-MM-YYYY): ")
        try:
            birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
            break
        except ValueError:
            print("\nInvalid date format. Please enter the date in DD-MM-YYYY format.")

    address = input("\nEnter your address (Street - Number - City - State): ")

    new_customer = NaturalPerson(cpf, name, birth_date, address)
    print(new_customer.get_info())

    
def account_creation():
    customer_exists = False
    balance = 0
    customer_cpf = ""
    withdraw_limit = 0

    customer_cpf = input("\nEnter the CPF this account will be vinculated to: ")
    for customer in Customer.customers:
            if customer_cpf == customer.cpf:
                customer_exists = True

    if not customer_exists:
        print("\nUnable to vinculate account to this CPF, because it is not yet registered.")
        return

    while True:
        try:
            balance = float(input("\nEnter the account's current balance: "))
            break
        except ValueError:
            print("\nEnter a number.")

    while True:
        try:
            withdraw_limit = float(input("\nEnter the account's withdraw limit: "))
            break
        except ValueError:
            print("\nEnter a number.")

    new_account = CheckingAccount(balance, customer_cpf, withdraw_limit)
    print(new_account.get_info())


def withdraw_operation():
    curr_account = find_account()

    if curr_account is None:
        return
    
    try:
        value = float(input("\nWithdrawal value: "))
    except ValueError:
        print("\nPlease, enter a number.")
        return

    curr_account.withdraw(value)


def deposit_operation():
    curr_account = find_account()

    if curr_account is None:
        return

    try:
        value = float(input("\nDeposit value: "))
    except ValueError:
        print("\nPlease, enter a number.")
        return

    curr_account.deposit(value)


def display_statement():
    curr_account = find_account()

    if curr_account is None:
        return
    
    curr_account.history.display_transactions()
    print()


def find_account():
    customer_exists = False
    account_exists = False
    curr_customer = None
    curr_account = None

    customer_cpf = input("\nEnter user's CPF: ")
    for customer in Customer.customers:
            if customer_cpf == customer.cpf:
                customer_exists = True
                curr_customer = customer
    if not customer_exists:
        print("\nUser not found.")
        return
    
    try:
        customer_account = int(input("\nEnter account's number: "))
    except ValueError:
        print("\nInvalid value.")
        return
    for account in curr_customer._accounts:
            if customer_account == account.number:
                account_exists = True
                curr_account = account
    if not account_exists:
        print("\nAccount not found.")
        return
    
    return curr_account


main()
