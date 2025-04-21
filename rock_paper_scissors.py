''' This is a Rock Papaer and Scissors game'''

import random
total_games=0
number_of_wins=0
number_of_draws=0
choices=["rock","paper","scissors"]

while True:
    random_no=random.randint(0,2)
    user_choice=input("\nEnter Rock/Paper/Scissors: (q to quit) ").lower()
    if user_choice=="q":
        break
    if user_choice not in choices:
        continue
    comp_choice=choices[random_no]
    if (comp_choice=="rock" and user_choice=="scissors") or (comp_choice=="scissors" and user_choice=="paper") or (comp_choice=="paper" and user_choice=="rock"):
        print("\nYou lose!")
        print(f"{comp_choice} beat your {user_choice}")
    elif comp_choice==user_choice:
        print("\nDraw")
        number_of_draws+=1
    else:
        print("\nYou won")
        print(f"Your {user_choice} beat {comp_choice}")
        number_of_wins+=1
    
