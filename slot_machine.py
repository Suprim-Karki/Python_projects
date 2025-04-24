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
symbol_values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+=values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machines(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(f"{column[row]} | ",end="")
            else:
                print(column[row])

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

def spin(balance):
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

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots,lines,bet,symbol_values)
    print(f"\nYou won ${winnings}")
    print(f"You won on lines: {winning_lines}")
    return winnings-total_bet

def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance is ${balance}")
        answer = input("Press enter to play (q to quit) : ")
        if answer.lower()=="q":
            break
        balance+=spin(balance)


    
main()