# BANKING PROGRAM

def show_menu():
    print("***********************************")
    print("     Banking Program     ")
    print("***********************************")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("***********************************")


def show_balance(balance):
    print("***********************************")
    print(f"Your balance is ${balance}")
    print("***********************************")


def deposit():
    print("***********************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("***********************************")

    if amount <= 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount


def withdraw(balance):
    print("***********************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("***********************************")

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <= 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("This is not a valid choice")

    print("***********************************")
    print("Thank you! Have a nice day.")
    print("***********************************")


if __name__ == "__main__":
    main()