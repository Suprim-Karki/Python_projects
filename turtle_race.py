import random
import turtle
import time

HEIGHT,WIDTH = 500,500
COLORS=["black","blue","red","orange","teal","green","maroon","purple","cyan","gold"]

def get_number_of_racers():
    while True:
        try:
            numbers=int(input("Enter the number of turtles: "))
            if 1<numbers<=10:
                break
            else:
                print("Please enter numbers 2-10\n")
        except ValueError:
            print("Enter a number from 2-10\n")
    return numbers

def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH// (len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)  
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2+50)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Rance")

def main():
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    turtles=create_turtles(colors)

main()