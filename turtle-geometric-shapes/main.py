import random
from turtle import Turtle, Screen

def make_shapes(n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)
    chosen_color = random.choice(colors)
    my_turtle.pencolor(chosen_color)


my_turtle  = Turtle()
my_screen = Screen()
colors = ["red", "blue", "yellow", "green", "orange", "purple", "yellow", "blue", "black", "grey"]

for i in range(3,11):
    make_shapes(n_sides= i)

my_screen.exitonclick()