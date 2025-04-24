import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1   

ROWS=3
COLS=3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get

def deposit():
    while True:
        try:
            amount=int(input("\nEnter the amount to deposit: "))
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Enter a valid number:")
    return amount

def get_number_of_lines():
    while True:
        try:
            lines=int(input(f"\nEnter the number of lines to bet on (1-{MAX_LINES}) : "))
            if 1<=lines<=MAX_LINES:
                break
            else:
                print(f"Amount must be between 1 and {MAX_LINES}")
        except ValueError:
            print("Enter a valid number:")
    return lines

def get_bet_amount():
    while True:
        try:
            bet=int(input(f"\nEnter the amount to bet on each line (${MIN_BET}-${MAX_BET}) : $"))
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        except ValueError:
            print("Enter a valid number:")
    return bet

def main():
    balance = deposit()
    lines=get_number_of_lines()

    while True:
        bet=get_bet_amount()
        total_bet = bet*lines
        if total_bet>balance:
            print(f"You do not have enough to bet. Your current balance is ${balance}")
        else:
            break
    print(f"\nYou are betting {bet} on {lines} lines.")
    print(f"The total bet is equal to {total_bet}")



main()