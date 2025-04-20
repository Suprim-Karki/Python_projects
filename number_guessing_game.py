''' This is a number guessting game'''

import random

# random.randrange(1,11)     #doesm't include 11
try:
    top_range = int(input("Enter the top range: "))
    if top_range<=0:
        print("Input a number greater than 0: ")
        quit()
    else:
        random_no = random.randint(top_range)     #includes 11


except ValueError:
    print("Input a whole number: ")