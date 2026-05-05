# SLOT MACHINE PROGRAM

import random

def spin_grid():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    grid = []

    for _ in range(3):
        row = [random.choice(symbols) for _ in range(3)]
        grid.append(row)

    return grid


def print_grid(grid):
    print("*************")
    for row in grid:
        print(" | ".join(row))
    print("*************")

def get_payout(grid, bet):
    total_payout = 0
    winning_rows = []
    
    for i, row in enumerate(grid):
        if row[0] == row[1] == row[2]:
            winning_rows.append(i + 1)

            if row[0] == '🍒':
                total_payout += bet * 3
            elif row[0] == '🍉':
                total_payout += bet * 4
            elif row[0] == '🍋':
                total_payout += bet * 5
            elif row[0] == '🔔':
                total_payout += bet * 10
            elif row[0] == '⭐':
                total_payout += bet * 20

    return total_payout, winning_rows
    

def main():
    balance = 100

    print("***********************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("***********************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        grid = spin_grid()
        print("Spinning...\n")
        print_grid(grid)

        payout, winning_rows = get_payout(grid, bet)

        if payout > 0:
            print(f"You won ${payout}")
            print(f"Winning rows: {winning_rows}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break
    
    print("********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")

if __name__ == "__main__":
    main()