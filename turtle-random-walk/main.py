import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

def change_turtle_appearance():
    #Assigning Random pen color
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_turtle.pencolor(r,g,b)

    # Changing Turtle's Speed,Pensize, hiding turtle
    my_turtle.speed("fastest")
    my_turtle.pensize(15)
    my_turtle.hideturtle()
    my_screen.bgcolor("black")  #changes color of screen to black


def move_turtle():
    my_turtle.forward(50)
    my_turtle.setheading(random.choice(headings))


my_screen = Screen()
my_turtle  = Turtle()

headings = [0,90,180,270]

for _ in range(101):
    change_turtle_appearance()
    move_turtle()

my_screen.exitonclick()