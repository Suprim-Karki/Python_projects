''' This is a Rock Papaer and Scissors game'''

import random
total_games=0
number_of_wins=0
number_of_draws=0
choices=["Rock","Paper","Scissors"]

while True:
    random_no=random.randint(1,3)
    user_choice=int(input("Enter 0 for Rock, 1 for Paper and 2 for scissors"))
