MAX_LINES=3

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
            amount=int(input("\nEnter the number of lines to bet on: "))
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        except ValueError:
            print("Enter a valid number:")
    return amount

def main():
    balance = deposit()


main()