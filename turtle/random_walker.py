import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
length = 20
thickness = 10
path_length = 200
directions = [0, 90, 180, 270]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    the_color = (r, g, b)
    return the_color


def random_direction():
    return random.choice(directions)


timmy.speed(0)
for i in range(0, path_length):

    tup = random_color()
    angle = random_direction()
    timmy.pencolor(tup)
    timmy.width(thickness)
    timmy.setheading(angle)
    timmy.forward(length)








screen = Screen()
screen.exitonclick()
