''' This is a number guessting game'''

import random

top_range = int(input("Enter the top range: "))

# random.randrange(1,11)     #doesm't include 11
random_no = random.randint(1,10)     #includes 11