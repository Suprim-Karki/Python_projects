''' This is a number guessting game'''

import random
guess=1

# random.randrange(1,11)     #doesm't include 11
try:
    top_range = int(input("Enter the top range: "))
    if top_range<=0:
        print("Input a number greater than 0: ")
        quit()
except ValueError:
    print("Input a whole number: ")
    quit()

while True:
    random_no = random.randint(1,top_range)     #includes top range too
    user_input=int(input("Guess the number: "))
    if user_input==random_no:
        print(f"You won\nYou got it in {guess} guesses")
        break
    else:
        guess+=1
        print(f"Correct answer was {random_no}\nTry Again\n")