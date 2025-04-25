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
    screen.title("Turtle Race")

def race_turtles(colors):
    turtles=create_turtles(colors)

    while True:
        for i,racer in enumerate(turtles):
            distance=random.randint(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[i]


def main():
    racers = get_number_of_racers()
    init_turtle()
    random.shuffle(COLORS)
    colors = COLORS[:racers]
    winner = race_turtles(colors)
    print(f"The winner is the turtle with color: {winner}")
    time.sleep(5)
main()