menu = '''
Enter the letter that corresponds to the desired action:

[d] Deposit
[w] Withdraw 
[s] Statement
[q] Quit

> '''

balance = 0
LIMIT = 500
num_withdraw = 0
WITHDRAW_LIMIT = 3
statement = []

def main():

    while True:
        option = input(menu).lower()

        match option:
            case 'd':
                print("DEPOSIT\n")
                deposit()
            case 'w':
                print("WITHDRAW\n")
                withdraw()
            case 's':
                print("STATEMENT\n")
                display_statement()
            case 'q':
                print("\nBye!")
                break
            case _:
                print("Invalid option. Try again.")


def deposit():
    global balance

    try:
        deposit_value = float(input("How much do you want to deposit?\n> "))
    except ValueError:
        print("\nInvalid value.")
        return
    
    if deposit_value < 0:
        print("\nYou can't deposit non-positive values.")
        return
    
    balance += deposit_value

    deposit_string = f"R$ {deposit_value:.2f}"
    statement.append({"Deposit": deposit_string})
        

def withdraw():
    global num_withdraw
    global balance
    
    if num_withdraw >= WITHDRAW_LIMIT:
        print("Withdrawal unavailable: you reached you daily limit.")
        return
    
    try:
        withdraw_value = float(input("How much do you want to withdraw?\n> "))
    except ValueError:
        print("\nInvalid value.")
        return

    if withdraw_value > 500:
        print("\nWithdrawal unavailable: can't withdraw more than R$ 500.00 at a time.")
        return
    
    if withdraw_value > balance:
        print("\nWithdrawal unavailable: insufficient balance.")
        return
    
    balance -= withdraw_value
    num_withdraw += 1

    withdraw_string = f"R$ {withdraw_value:.2f}"
    statement.append({"Withdrawal": withdraw_string})


def display_statement():

    if len(statement) > 0:
        for item in statement:
            for part in item:
                print(f"- {part}: {item[part]}")
    else:
        print("\nNo transactions were made in your account.")

    print(f"\nCurrent balance: R$ {balance:.2f}")


main()
