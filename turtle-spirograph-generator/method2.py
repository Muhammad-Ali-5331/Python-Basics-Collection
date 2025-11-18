import random
import turtle
from turtle import Turtle, Screen


def change_turtle_appearance():
    #Assigning Random pen color
    r = random.randint(0,255) ## 255 not 256 because randint takes the upper limit unlike range function
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_turtle.color(r,g,b)

    # Changing Turtle's Speed
    my_turtle.speed("fastest")
    my_screen.bgcolor("black")  #changes color of screen to black


def draw_spirograph():
    angle = 0
    for _ in range(360):
        change_turtle_appearance()
        my_turtle.circle(100)
        my_turtle.left(angle)
        angle += 1


my_screen = Screen()
my_turtle  = Turtle()
turtle.colormode(255)

draw_spirograph()

my_screen.exitonclick()