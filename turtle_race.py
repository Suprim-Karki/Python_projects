import random
import turtle
import time


def choose_turtle():
    colors=["black","blue","red","brown","pink"]
    turtles=[]
    while True:
        try:
            numbers=int(input("Enter the number of turtles: "))
            if 1<numbers<=10:
                random.shuffle(colors)
                for i in range(numbers):
                    turtles.append(colors[i])
                break
            else:
                print("Please enter numbers 2-10\n")
        except ValueError:
            print("Enter a number from 2-10\n")
    return turtles


def main():
    turtles = choose_turtle()
    print(turtles)

main()