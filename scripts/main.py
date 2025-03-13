from time import sleep
from classes import *

# customer creation
customer1 = NaturalPerson("12345678901", "Link", "29/11/2003", "Kokiri Forest")
customer2 = NaturalPerson("98765432109", "Zelda", "12/04/2003", "Hyrule Castle")

# account creation
account1 = CheckingAccount(balance=1000.00, customer_cpf="12345678901", withdraw_limit=1000.00, dayly_limit=5)
account2 = CheckingAccount(balance=2000.00, customer_cpf="12345678901", withdraw_limit=2000.00, dayly_limit=10)

account3 = CheckingAccount(balance=1250.00, customer_cpf="98765432109", withdraw_limit=1500.00, dayly_limit=8)
account4 = CheckingAccount(balance=3500.00, customer_cpf="98765432109", withdraw_limit=2500.00, dayly_limit=15)

# customer display
print("\nCUSTOMERS:")
Customer.display_customers()
sleep(5)

# balance display
print("\nBALANCE:\n")
print(account1.balance)
print(account2.balance)
print(account3.balance)
print(account4.balance)
sleep(5)

# deposit
account1.deposit(150.00)
account2.deposit(1000.00)
account3.deposit(50.00)
account4.deposit(700.00)
print("\nBALANCE - deposit:\n")
print(f"+R$ 150.00 -> {account1.balance}")
print(f"+R$ 1000.00 -> {account2.balance}")
print(f"+R$ 50.00 -> {account3.balance}")
print(f"+R$ 700.00 -> {account4.balance}")
sleep(5)

# withdrawal
account1.withdraw(200.00)
account2.withdraw(475.00)
account3.withdraw(450.00)
account4.withdraw(750.00)
print("\nBALANCE - withdrawal:\n")
print(f"-R$ 200.00 -> {account1.balance}")
print(f"-R$ 475.00 -> {account2.balance}")
print(f"-R$ 450.00 -> {account3.balance}")
print(f"-R$ 750.00 -> {account4.balance}")
sleep(5)

# display accounts info
print("\nACCOUNTS INFO:")
Account.display_accounts()
sleep(5)

# display transactions
print("\nTRANSACTIONS:\n")
account1._history.display_transactions()
print()
account2._history.display_transactions()
print()
account3._history.display_transactions()
print()
account4._history.display_transactions()
