''' PIG game '''

import random

def roll():
    min=1
    max=6
    roll = random.randint(min,max)
    return roll

while True:
    try:
        players=int(input("Enter the number of players (2-4): "))
        if 2 <= players <= 4:
            break
        else:
            print("\nGive a number from 2-4: ")
    except ValueError:
        print("\nGive a number from 2-4: ")

max_score=50
player_score = [0 for _ in range(players)]

while max(player_score)<max_score:
    for i in range(players):
        current_score=0
        while True:
            print(f"\nPlayer {i+1} Turn:")
            print(f"Your total score is {player_score[i]}\n")
            should_roll = input("Would you like to roll? (y): ")
            if should_roll.lower()!="y":
                break
            value = roll()
            if value == 1:
                print("You rolled 1! Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print(f"You rolled {value}")
            print(f"Your score is {current_score}")
        player_score[i]+=current_score
        print(f"Your total score is {player_score[i]}")

max_score=max(player_score)
winnind_idx=player_score.index(max_score)
print(f"Player {winnind_idx+1} is the winner with a score of {max_score}")