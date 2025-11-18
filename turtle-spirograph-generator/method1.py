import random
import turtle
from turtle import Turtle, Screen


def change_turtle_appearance():
    #Assigning Random pen color
    r = random.randint(0,255) ## 255 not 256 because randint takes the upper limit unlike range function
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_turtle.color(r,g,b)
    #my_turtle.pencolor(r,g,b)

    # Changing Turtle's Speed
    my_turtle.speed(20)
    #my_screen.bgcolor("black")  #changes color of screen to black


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        change_turtle_appearance()
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


my_screen = Screen()
my_turtle  = Turtle()
turtle.colormode(255)

draw_spirograph(1)

my_screen.exitonclick()