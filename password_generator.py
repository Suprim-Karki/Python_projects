import random
import string

def generate_password(length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters = letters
    if numbers:
        characters+=digits
    if special:
        characters+=special

    pwd=""
    meets_criteria=False
    has_numbers=False
    has_special=False
    
    while not meets_criteria or len(pwd)<length:
        new_char=random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_numbers=True
        if new_char in special:
            has_special=True
        meets_criteria=True
        if numbers:
            meets_criteria=has_numbers
        if special_characters:
            meets_criteria=meets_criteria and has_special

    return pwd

length=int(input("Enter the length of pwd: "))
number = input("Do you want to include numbers(y/n): ").lower()=="y"
special_characters = input("Do you want to include special_characters(y/n): ").lower()=="y"
pwd=generate_password(length,number,special_characters)
print(f"\nThe generated password is : {pwd}\n")

        