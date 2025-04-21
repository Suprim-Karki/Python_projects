''' This is a Rock Papaer and Scissors game'''

import random
total_games=0
number_of_wins=0
number_of_draws=0
number_of_loss=0
choices=["rock","paper","scissors"]

while True:
    random_no=random.randint(0,2)
    user_choice=input("\nEnter Rock/Paper/Scissors: (q to quit) ").lower()
    if user_choice=="q":
        print(f"\nYou won {number_of_wins} times")
        print(f"Computer won {number_of_loss} times")
        print(f"You drew {number_of_draws} times")
        break
    if user_choice not in choices:
        print("\nInvalid option, try again!")
        continue
    comp_choice=choices[random_no]
    if (comp_choice=="rock" and user_choice=="scissors") or (comp_choice=="scissors" and user_choice=="paper") or (comp_choice=="paper" and user_choice=="rock"):
        print("\nYou lose!")
        print(f"{comp_choice} beat your {user_choice}")
        number_of_loss+=1
    elif comp_choice==user_choice:
        print("\nDraw")
        number_of_draws+=1
    else:
        print("\nYou won")
        print(f"Your {user_choice} beat {comp_choice}")
        number_of_wins+=1
    
